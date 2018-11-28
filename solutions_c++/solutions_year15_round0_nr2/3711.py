#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[1010];
void Solve()
{
    int T,cnt=0;
    int n,max1,min1,sum;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            max1=max(max1,a[i]);
        }
        min1=max1;
        for(int i=1;i<=min1;i++)
        {
            sum=i;
            for(int j=0;j<n;j++)
            {
                if(a[j]>i)
                {
                    if(a[j]%i==0)sum+=(a[j]/i-1);
                    else sum+=(a[j]/i);
                }
            }
            min1=min(min1,sum);
        }
        printf("Case #%d: %d\n",++cnt,min1);
    }
}
int main()
{
    freopen("3.in","r",stdin);
    freopen("3.out","w",stdout);
    Solve();
    return 0;
}
