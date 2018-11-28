#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;

double a[5000],b[5000];
bool v[1005];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lf",a+i);
        sort(a,a+n);
        for(int i=0;i<n;i++)
            scanf("%lf",b+i);
        sort(b,b+n);
        int p=n-1,c1=0,c2=0;
        memset(v,0,sizeof(v));
        for(int i=0;i<n;i++)
        {
            int o=-1;
            for(int j=0;j<n;j++)
                if(v[j]==0&&a[j]>b[i])
                {
                    o=j;
                    v[j]=1;
                    c1++;
                    break;
                }
            if(o==-1)
            {
                for(int j=0;j<n;j++)
                    if(v[j]==0)
                    {
                        v[j]=1;
                        break;
                    }
            }
        }
        p=n-1;
        memset(v,0,sizeof(v));
        for(int i=0;i<n;i++)
        {
            int o=-1;
            for(int j=0;j<n;j++)
                if(v[j]==0&&b[j]>a[i])
                {
                    o=j;
                    v[j]=1;
                    break;
                }
            if(o==-1)
            {
                c2++;
                for(int j=0;j<n;j++)
                    if(v[j]==0)
                    {
                        v[j]=1;
                        break;
                    }
            }
        }
        printf("Case #%d: %d %d\n",ti++,c1,c2);
    }
    return 0;
}
