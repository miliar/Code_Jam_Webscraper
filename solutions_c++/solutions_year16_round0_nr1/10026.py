#include<bits/stdc++.h>
using namespace std;
#define pi (2.0*acos(0.0))
#define eps 1e-6
#define ll long long
#define inf (1<<30)
#define vi vector<int>
#define vll vector<ll>
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
#define all(v) v.begin() , v.end()
#define me(a,val) memset( a , val ,sizeof(a) )
#define pb(x) push_back(x)
#define pii pair<int,int> 
#define mp(a,b) make_pair(a,b)
#define Q(x) (x) * (x)
#define L(x) ((x<<1) + 1)
#define R(x) ((x<<1) + 2)
#define M(x,y) ((x+y)>>1)
#define fi first
#define se second
#define MOD 1000000007
#define ios ios::sync_with_stdio(0)
#define N 11

bool vis[N];

int main(){
	int tc;
	int r = sc(tc);
	for(int tt = 1 ; tt <= tc ; tt++){
		printf("Case #%d: ",tt);
		ll n;
		r = scl(n);
		if( n == 0 ) printf("INSOMNIA\n");
		else{
			me(vis,0);
			int have = 0 , ans = 1;
			while( 1 ){
				ll m = n * ans;
				while( m ){
					r = m % 10;
					if( !vis[r] ){
						vis[r] = 1;
						have++;
					}
					vis[r] = 1;
					m /= 10;
				}
				if( have == 10 ) break;
				ans++;
			}
			printf("%lld\n",n*ans);
		}
	}
}
