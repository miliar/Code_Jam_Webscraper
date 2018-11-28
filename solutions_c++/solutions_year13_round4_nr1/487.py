#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<string>
#include<string.h>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<map>
#include<set>
#include<bitset>
#include<iostream>
#include<sstream>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < n; i++)
#define rrep(i,n) for(int i = 1; i <= n; i++)
#define drep(i,n) for(int i = n-1; i >= 0; i--)
#define each(c,it) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y);
#define mins(x,y) x = min(x,y);
#define pb push_back
#define snuke srand((unsigned)time(NULL))
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;

const int MX = 100005, INF = 1000000000, mod = 1000000009;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-9;
const int dx[4] = {-1,0,1,0}, dy[4] = {0,-1,0,1}; //<^>v

P d[2005];
P p[1005]; int ps;

int main(){
	int te, n, m, s, t, x; ll ans, sum;
	scanf("%d",&te);
	rrep(ti,te){
		scanf("%d%d",&n,&m);
		sum = ans = 0;
		rep(i,m){
			scanf("%d%d%d",&s,&t,&x);
			d[i*2] = P(s,-x);
			d[i*2+1] = P(t,x);
			sum += (ll)x*((ll)n*2-(t-s)+1)*(t-s)/2;
		}
		sort(d,d+m*2);
		ps = -1;
		rep(i,m*2){
			s = d[i].fi; x = d[i].se;
			if(x < 0){
				p[++ps] = P(s,-x);
			} else {
				while(x){
					if(p[ps].se <= x){
						t = s-p[ps].fi;
						ans += (ll)p[ps].se*((ll)n*2-t+1)*t/2;
						x -= p[ps].se;
						ps--;
					} else {
						t = s-p[ps].fi;
						ans += (ll)x*((ll)n*2-t+1)*t/2;
						p[ps].se -= x; x = 0;
					}
				}
			}
		}
		
		printf("Case #%d: %lld\n",ti,sum-ans);
	}
	return 0;
}





