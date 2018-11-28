#include <bits/stdc++.h>
#define ll             long long
#define pi             pair <int,int>
#define pl             pair <ll,ll>
#define ps             pair <string,string>
#define vi         vector <int>
#define vl             vector <ll>
#define vpi            vector <pi>
#define vpl            vector <pl>
#define st             string
#define vs             vector <st>
#define f(i,a,b)       for(ll i=(a);i<(b);i++)
#define fd(i,a,b)      for(ll i=(a);i>(b);i--)
#define Max(a,b)       ((a)>(b)?(a):(b))
#define Min(a,b)       ((a)<(b)?(a):(b))
#define x              first
#define y              second
#define si(a)          scanf("%d",&a)
#define sii(a,b)       scanf("%d %d",&a,&b)
#define siii(a,b,c)    scanf("%d %d %d",&a,&b,&c)
#define sl(a)          scanf("%lld",&a)
#define sll(a,b)       scanf("%lld %lld",&a,&b)
#define slll(a,b,c)    scanf("%lld %lld %lld",&a,&b,&c);
#define pf             printf
#define pfi(n)         printf("%d\n",n)
#define pfl(n)         printf("%lld\n",n)
#define pfls(n)        printf("%lld ",n)
#define pfci(n,ans)    printf("Case %lld: %d\n",n,ans)
#define pfcl(n,ans)    printf("Case %lld: %lld\n",n,ans)
#define pfcd(n,ans)    printf("Case %lld: %lf\n",n,ans)
#define pb             push_back
#define all(v)         v.begin(),v.end()
#define mem(a,v)       memset(a,v,sizeof(a))
#define INF 1e18
#define MAX 107
#define MOD 1000000007
#define LG  16
#define mid ((l+r)/2)
#define H(i,j) (i*107+j)
#define IN(n) (2*(n)-1)
#define OUT(n) (2*(n))
using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	ll T;
	sl(T);
	f(t,1,T+1){
		ll N;
		sl(N);
		vpl v;
		f(i,0,N){
			ll a;
			sl(a);
			v.pb(pl(a,i));
		}
		sort(all(v));
		reverse(all(v));
		pf("Case #%lld:",t);
		f(i,0,v[0].x-v[1].x){
			cout<<' '<<(char)('A'+v[0].y);
		}
		fd(i,v.size()-1,1){
			f(j,0,v[i].x){
				cout<<' '<<(char)('A'+v[i].y);
			}
		}
		f(i,0,v[1].x){
			cout<<' '<<(char)('A'+v[0].y)<<(char)('A'+v[1].y);
		}
		cout<<endl;
	}
}