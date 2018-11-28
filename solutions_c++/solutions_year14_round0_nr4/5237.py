#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstring>
using namespace std;
double a[1005],b[1005];
int used[1005],used1[1005];
int main()
{
    freopen("intput.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,n,i,j;
    scanf("%d",&T);
    int k=0;
    while(T--)
    {
        memset(used,0,sizeof(used));
        memset(used1,0,sizeof(used1));
        scanf("%d",&n);
        for(i=0;i<n;i++)
        scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
        scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int h=0;
        int ans1=0,ans2=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(used[j]==0)
                {
                    if(a[i]>b[j])
                    {
                        used[j]=1;
                        ans1++;
                        break;
                    }
                    else
                    {
                        used[n-h-1]=1;
                        h++;
                        break;
                    }
                }
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(a[i]<b[j]&&used1[j]==0)
                {
                    used1[j]=1;
                    break;
                }
            }
        }
        for(i=0;i<n;i++)
        if(used1[i]==0)
        ans2++;
        printf("Case #%d: %d %d\n",++k,ans1,ans2);
    }
    return 0;
}
