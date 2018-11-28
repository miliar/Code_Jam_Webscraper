#include <iostream>
#include<cstdio>
#include<math.h>

using namespace std;
int dp[1005];

void pre()
{
    int s,r,n,num,l,i;
    s=0;
    l=0;
    for(i=1;i<=sqrt(1000);i++)
    {
        n=i;s=0;
        while(n>0)
        {
            r=n%10;
            n=n/10;
            s=(s*10)+r;
        }
        if(i==s)
        {
            n=i*i;
            num=n;
            s=0;
            while(n>0)
            {
                r=n%10;
                n=n/10;
                s=(s*10)+r;
            }
            if(num==s)
            {
                for(int k=l+1;k<num;k++)
                dp[k]=dp[k-1];
                dp[num]=dp[num-1]+1;
                l=num;
            }
        }
    }
    for(int k=l+1;k<=1000;k++)
    dp[k]=dp[k-1];
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.in","w",stdout);
    int test,a,b,k;
    pre();
    scanf("%d",&test);
    for(k=1;k<=test;k++)
    {
        scanf("%d%d",&a,&b);
        printf("Case #%d: ",k);
        printf("%d\n",dp[b]-dp[a-1]);
    }
    return 0;
}
