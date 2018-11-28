#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
#define f first
#define s second
#define si(x)   scanf("%d",&x)
#define sl(x)   scanf("%lld",&x)
#define CLR(x)  memset(x,0,sizeof(x))
#define RESET(x,a) memset(x,a,sizeof(x))
#define pi pair<int,int>
#define pb push_back
#define mp make_pair
#define debug(x) cerr<<">value ("<<#x<<") : "<<x<<endl;

int a[15];

void f(ll n)
{
    while(n)
    {
        int c=(int)(n%10LL);
        a[c]=1;
        n/=10LL;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-out.txt","w",stdout);
    int tt,t,j;
    ll n,m,i;
    si(tt);
    for(t=1;t<=tt;t++)
    {
        sl(n);
        CLR(a);
        m=n;
        if(m==0)
        {
            printf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        while(1)
        {
            f(m);
            j=0;
            for(i=0;i<10;i++)
                if(a[i])j++;
            if(j==10)break;
            m=m+n;
        }
        printf("Case #%d: %lld\n",t,m);
    }
    return 0;
}
