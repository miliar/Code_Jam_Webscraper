#include <bits/stdc++.h>
#define ll             long long
#define pi             pair <int,int>
#define pl             pair <ll,ll>
#define ps             pair <string,string>
#define vi	       vector <int>
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
#define pfci(n,ans)    printf("Case %d: %d\n",n,ans)
#define pfcl(n,ans)    printf("Case %d: %lld\n",n,ans)
#define pb             push_back
#define all(v)         v.begin(),v.end()
#define mem(a,v)       memset(a,v,sizeof(a))

using namespace std;
int main(){
    ifstream fin ("A-large.in");
    ofstream fout ("A.out");
    ll T;
    fin>>T;
    f(t,1,T+1){
        ll sm;
        st s;
        fin>>sm>>s;
        ll sum=0;
        ll ans=0;
        f(i,0,sm){
            sum+=(s[i]-'0');
            if (sum<i+1) ans+=(i+1-sum), sum=i+1;
        }
        fout<<"Case #"<<t<<": "<<ans<<endl;
    }
}
