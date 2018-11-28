#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>

using namespace std;

bool v[10];

int main()
{
   // freopen("input.txt","r",stdin);
   // freopen("output.txt","w",stdout);
    int t;
    long long n,ans,sum;
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",cas);
            continue;
        }
        memset(v,0,sizeof(v));
        sum=0;
        for(long long i=1;i<=900;i++)
        {
            long long k=n*i;
            while(k>0)
            {
                if(v[k%10]==0)
                {
                    v[k%10]=1;
                    sum+=k%10+1;
                }
                k/=10;
            }
            if(sum==55)
            {
                ans=n*i;
                break;
            }
        }
        printf("Case #%d: %lld\n",cas,ans);
    }
    return 0;
}