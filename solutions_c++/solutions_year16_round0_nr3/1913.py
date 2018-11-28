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

int main(){
    freopen("big.txt","w",stdout);
    string core;
    string trophy = " 3 4 5 6 7 8 9 10 11";
    core.pb('1');
    f(i,0,30) core.pb('0');
    core.pb('1');
    ll cnt=0;
    pf("Case #1:\n");
    for(ll i=1;i<31;i+=2){
        for(ll i_=i+2;i_<31;i_+=2){
            for(ll j=2;j<31;j+=2){
                for(ll j_=j+2;j_<31;j_+=2){
                    cnt++;
                    string tmp=core;
                    tmp[i]=tmp[i_]=tmp[j]=tmp[j_]='1';
                    cout<<tmp<<trophy<<endl;
                    if(cnt==500){
                        return 0;
                    }
                }
            }
        }
     }
}
