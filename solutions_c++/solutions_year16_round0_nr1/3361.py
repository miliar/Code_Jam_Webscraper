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
int a[11],cnt=0;
ll solve(ll n)
{
    ll i,f=0;
    for(i=1;f!=1;i++)
    {
        ll z=n*i;
        while(z)
        {
            int r=z%10;
            if(!a[r])
            {
                cnt++;
                a[r]=1;
            }
            z/=10;
        }
        if(cnt==10)
            return n*i;
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,n=0,T=0;
    sl(t);
    while(t--)
    {
        memset(a,0,sizeof(a));
        cnt=0;
        sl(n);
        if(n)
            printf("Case #%lld: %lld\n",++T,solve(n));
        else
            printf("Case #%lld: INSOMNIA\n",++T);
    }
    return 0;
}
