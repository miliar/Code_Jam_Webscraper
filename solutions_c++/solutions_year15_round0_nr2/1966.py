#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
using namespace std;
int casenum;
int n;
int a[1005];
int main(void)
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&casenum);
    for(int k=1;k<=casenum;k++)
    {
        memset(a,0,sizeof(a));
        scanf("%d",&n);
        int zuida=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            zuida=max(zuida,a[i]);
        }
        int ans=zuida;
        for(int i=1;i<=zuida;i++)
        {
            int sum=i ;
            for(int j=1;j<=n;j++)
            {
                if(a[j]>i)
                {
                    if(a[j]%i==0)
                        sum+=(a[j]/i-1) ;
                    else
                        sum+=(a[j]/i) ;
                }
            }
            ans=min(ans,sum) ;
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}

