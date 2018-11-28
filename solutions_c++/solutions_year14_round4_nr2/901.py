#include <string.h>
#include <algorithm>
#include <stdio.h>
#define maxn 1010
using namespace std;
int a[maxn];
int left[maxn],right[maxn];
int main()
{
    freopen("dd.txt","r",stdin);
   // freopen("out.txt","w+",stdout);
    int ncase,T=0;
    scanf("%d",&ncase);
    while(ncase--)
    {
        printf("Case #%d: ",++T);
        int n,ma=0,po;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            if(a[i]>ma)
            {
                ma=a[i];
                po=i;
            }
        }
        right[0]=left[0]=0;
        int num=1;
        for(int i=1;i<=n;i++)
        {
            if(i==po)
            continue;
            int tmp=0;
            for(int j=1;j<i;j++)
            {
                if(j==po)
                continue;
                if(a[j]>a[i])
                tmp++;
            }
            left[num]=tmp;
            left[num]+=left[num-1];
            num++;
        }
        num=1;
        for(int i=n;i>=1;i--)
        {
            if(i==po)
            continue;
            int tmp=0;
            for(int j=n;j>i;j--)
            {
                if(j==po)
                continue;
                if(a[j]>a[i])
                tmp++;
            }
            right[num]=tmp+right[num-1];
            num++;
        }
        for(int i=1;i<=n-1;i++)
        printf("%d ",left[i]);
        printf("\n");
        for(int i=1;i<=n-1;i++)
        printf("%d ",right[i]);
        printf("\n");
        int ans=10000000;
        for(int i=1;i<=n;i++)
        {
            int tmp=po-i;
            if(tmp<0)
            tmp=-tmp;
            tmp+=left[i-1];
            tmp+=right[n-i];
            ans=min(ans,tmp);
        }
        printf("%d\n",ans);
    }

    return 0;
}
