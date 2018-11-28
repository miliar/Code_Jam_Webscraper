#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define SF scanf
#define PF printf
#define INP          freopen("A-large.in", "r", stdin);
#define OUT          freopen("A-small.out", "w", stdout);
int a[15];
int main()
{
    int n,t,i,j,k,n1,c1,f;
    ll ans,m;
    INP;
    OUT;
    SF("%d",&n);
    for(t=1;t<=n;t++)
    {
        c1=1;
        for(i=0;i<10;i++)
        {
            a[i]=0;
        }
        SF("%d",&n1);
        ans=n1;
        while(ans!=0)
        {
            ans=c1*n1;
            m=ans;
            while(m!=0)
            {
                k=m%10;
                a[k]=1;
                m=m/10;
            }
            f=0;
            for(i=0;i<10;i++)
            {
                if(a[i]==0)
                {
                    f=1;
                    break;
                }
            }
            if(f==0)
            {
                break;
            }
            c1++;
        }
        if(ans==0)
        {
            PF("Case #%d: INSOMNIA\n",t);
        }
        else
        {
            PF("Case #%d: %lld\n",t,ans);
        }

    }
    return 0;
}
