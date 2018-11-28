#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int a[1005];
int main()
{
    int T,n;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int k=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        int ma=-1;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            ma=max(ma,a[i]);
        }
        int ans=0;
        int maa=ma;
        for(int i=1;i<=ma;i++)
        {
            ans=i;
            for(int j=1;j<=n;j++)
            {
                if(a[j]>i)
                {
                    if(a[j]%i==0)
                    ans+=(a[j]/i-1);
                    else
                    ans+=a[j]/i;
                }
            }
           maa=min(maa,ans);
        }

        printf("Case #%d: %d\n",++k,maa);
    }
    return 0;
}
