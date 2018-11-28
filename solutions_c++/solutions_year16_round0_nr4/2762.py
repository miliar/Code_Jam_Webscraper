#include<bits/stdc++.h>
#define ll long long int
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
int Set(int n,int pos) {return n | (1<<pos);}
int Reset(int n,int pos){return n & ~(1<<pos);}
int Check(int n,int pos){return n & (1<<pos);}
using namespace std;
ll pow(ll n,ll idx)
{
    ll i,ans;
    for(ans=1,i=1;i<=idx;i++)
    {
        ans*=n;
    }
    return ans;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,T=0,K,C,S,i,j,k;
    sl(t);
    while(t--)
    {
        sl(K); sl(C); sl(S);
        printf("Case #%lld:",++T);
        for(i=1;i<=K;i++)
            printf(" %lld",i);
        printf("\n");
    }
    return 0;
}
