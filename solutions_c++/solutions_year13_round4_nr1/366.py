#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;
#define For(i,n) for(int i=0;i<n;i++)
#define sz(i) int(i.size())
#define mst(i,n) memset(i,n,sizeof(i))
#define eps 1e-4
#define MOD 1000000007
#define LL long long
#define pi acos(-1)
#define ALL(n) n.begin(),n.end()
#define pb push_back
#define iFor(i,n) for(typeof(n.begin()) i=n.begin();i!=n.end();i++)

pair<LL, LL>inp[1005];
int p1=0;
pair<LL, LL>outp[1005];
int p2=0;

LL cnt(LL t){
    return t*(t-1)/2;
}
const LL mod = 1000002013LL;
int main(){
	int ca,cc=0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&ca);
	while(ca--){
        LL n,m;
        cin>>n>>m;
        LL ans1 = 0, ans2 = 0;
        p1 = p2 = 0;
        For(i,m){
            LL o,e,p;
            cin>>o>>e>>p;
            ans1 += cnt(e-o) % mod * p % mod;
            ans1 %= mod;
            inp[i] = make_pair(o, p);
            outp[i] = make_pair(e, p);
        }
        sort(inp, inp+m);
        sort(outp, outp+m);
        stack<pair<LL, LL> >st;
        For(j, m){
            while(p1<m&&inp[p1].first<=outp[j].first){
                st.push(inp[p1++]);
            }
            while(outp[j].second > 0){
                LL t = min(st.top().second, outp[j].second);
                outp[j].second -= t;
                st.top().second -= t;
                ans2 += cnt(outp[j].first - st.top().first) % mod * t % mod;
                if(st.top().second == 0){
                    st.pop();
                }
            }
        }
        LL ans = ((ans2 - ans1) % mod + mod ) % mod;
        cout<<"Case #"<< ++cc <<": "<<ans<<endl;
	}
	return 0;
}
