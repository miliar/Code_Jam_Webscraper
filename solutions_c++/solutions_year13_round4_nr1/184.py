#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------


bool isp(int n) {
	for(int i=2;i*i<=n;i++) if(n%i==0) return false;
	return true;
}

const int mod = 1000002013;

int getPaid(int n, int dis) {
	return (n + (n-dis+1))*(LL)dis/2 % mod;
}

struct DD{
	int x, sign, p;
	DD(int _x=0, int _sign =0, int _p=0) {
		x = _x;
		sign = _sign;
		p = _p;
	}
	bool operator<(const DD &b)const{
		if(x != b.x) return x < b.x;
		return sign > b.sign;
	}
};

int main() {
	freopen("F:/TDDOWNLOAD/A-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/A-large.out", "w", stdout);

	int T;
	cin>>T;
	rep(te, 1, T+1) {
		int N, M; cin>>N>>M;
		vector<DD> v;
		int sum = 0;
		rep(i, 0, M) {
			int l, r, p;
			cin>>l>>r>>p;
			v.push_back(DD(l, 1, p));
			v.push_back(DD(r, -1, p));
			sum = (sum + getPaid(N, r-l)*(LL)p) % mod;
		}
		sort(all(v));

		int sum1 = 0;
		vector<PII> left; //start p
		rep(i, 0, sz(v)) {
			if(v[i].sign == 1) {
				left.push_back(PII(v[i].x, v[i].p));
			} else {
				sort(all(left));
				//reverse(all(left));
				for(int j=sz(left)-1;j>=0;j--) {
					if(left[j].second <= v[i].p) {
						int p = left[j].second;
						v[i].p -= p;
						sum1 = (sum1 + getPaid(N, v[i].x-left[j].first)*(LL)p) % mod;
						left.pop_back();
					} else {
						int p = v[i].p;
						v[i].p -= p;
						left[j].second -= p;
						sum1 = (sum1 + getPaid(N, v[i].x-left[j].first)*(LL)p) % mod;
					}
					if(v[i].p == 0) break;
				}
			}
		}
		printf("Case #%d: %d\n", te, ((sum-sum1)%mod+mod)%mod);
	}
}