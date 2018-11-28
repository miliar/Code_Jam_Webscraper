//kopyh
#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define N 1123456
using namespace std;
long long n,m,sum,res,flag;
int a[11];
int main()
{
    long long i,j,k,cas,T,t,x,y,z;
    #ifndef ONLINE_JUDGE
        freopen("in.in","r",stdin);
        freopen("out.out","w",stdout);
    #endif
    scanf("%I64d",&T);
    cas=0;
    while(T--)
    {
        scanf("%I64d",&n);
        memset(a,0,sizeof(a));
        if(!n)
        {
            printf("Case #%I64d: INSOMNIA\n",++cas);
            continue;
        }
        m=0;sum=0;
        while(m<10)
        {
            sum+=n;
            t=sum;
            while(t)
            {
                if(a[t%10]==0)a[t%10]=1,m++;
                t/=10;
            }
        }
        printf("Case #%I64d: %I64d\n",++cas,sum);
    }
    return 0;
}
