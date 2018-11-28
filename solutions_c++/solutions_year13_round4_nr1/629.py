#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <map>
using namespace std;
typedef long long LL;
const int maxn = 1000 + 10;
const LL mod = 1000002013;
map<LL, LL> p;
pair<LL, LL> s[maxn];
int ss;
LL n;
LL cost(LL x, LL y){
	LL l = y - x;
	LL p1 = n+n+1-l;
	LL p2 = l;
	if (p1%2 == 0){
		p1/=2;
	}else{
		p2/=2;
	}
	return (p1%mod * p2)% mod;
}
int main(){
	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);
	int T;
	cin>>T;
	int cas = 0;
	while (T--){
		cin>>n;
		int m;
		cin>>m;
		LL oricost = 0;
		p.clear();
		for (int i = 0; i<m; i++){
			LL x, y, z;
			cin>>x>>y>>z;
			p[x]+=z;
			p[y]-=z;
			oricost = (oricost + cost(x, y)*z%mod);
		}
		ss = 0;
		LL tot = 0;
		int j = 0;
		for (map<LL, LL>::iterator it = p.begin(); it!=p.end(); it++){
			if (it->second > 0){
				s[ss++] = *it;
			}else{
				LL remain = -it->second;
				while (remain){
					LL k = min(s[ss-1].second, remain);
					tot = (tot + cost(s[ss-1].first, it->first)*k%mod)%mod;
					remain -=k;
					s[ss-1].second -=k;
					if (s[ss-1].second == 0){
						ss--;
					}
				}
			}
		}
		cas++;
		cout<<"Case #"<<cas<<": ";
		cout<<((oricost - tot)%mod + mod)%mod<<endl;
	}
	return 0;
}
