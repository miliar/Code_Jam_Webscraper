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
#define PI 2*acos(0.0)
#define un (PI/180)

using namespace std;

ll get(ll n){
    bool vis[10];
    mem(vis,false);
    ll m=0, cnt=0, n_=n;
    while(cnt<10){
        m++;
        ll n=m*n_;
        while(n){
            ll d=n%10;
            if(!vis[d]){
                vis[d]=true;
                cnt++;
            }
            n/=10;
        }
    }
    return m*n_;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("AoutL.txt","w",stdout);
    ll T;
    sl(T);
    f(t,1,T+1){
        ll n;
        sl(n);
        pf("Case #%lld: ",t);
        if(!n){
            pf("INSOMNIA\n");
        }
        else{
            pfl(get(n));
        }
    }
}
