#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mod 1000000007
#define bitcount    __builtin_popcountll
#define pb push_back
int main()
{
    freopen("codejamcountingsheepin.txt","r",stdin);
    freopen("codejamcountingsheepout1.txt","w",stdout);
    int t,n,i,j,k,a[12],cnt,x;
    sd(t);
    for(x=1;x<=t;x++)
    {
        sd(n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",x);
            continue;
        }
        cnt=0;
        j=0;
        for(i=0;i<=9;i++)
            a[i]=0;
        while(cnt!=10)
        {
            j+=n;
            k=j;
            while(k!=0)
            {
                i=k%10;
                if(a[i]==0)
                {
                    a[i]=1;
                    cnt++;
                }
                k/=10;
            }
        }
        printf("Case #%d: %d\n",x,j);
    }
    return 0;
}
