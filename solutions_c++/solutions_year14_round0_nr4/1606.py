#include<stdio.h>
#include<string.h>
#include<algorithm>
#define maxn 1008
using namespace std;
double a[maxn],b[maxn];
int mark[maxn];
int main()
{
    int i,j,k,n,t,cas=1;

    //freopen("D-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++) scanf("%lf",a+i);
        sort(a,a+n);
        for(i=0;i<n;i++) scanf("%lf",b+i);
        sort(b,b+n);
        memset(mark,0,sizeof(mark));
        int res1=0,res2=0;
        for(k=i=n-1,j=0;i>=j;i--,k--)
        {
            while(k>=0&&a[i]<=b[k])
            {
                j++;
                k--;
            }
            if(k>=0) res1++;
        }
        for(i=n-1;i>=0;i--)
        {
            int temp=-1;
            for(j=n-1;j>=0;j--)
            {
                if(mark[j]) continue;
                if(b[j]>a[i]) temp=j;
            }
            if(temp==-1)
            {
                for(j=0;j<n;j++) if(!mark[j]) break;
                mark[j]=1;
                res2++;
            }
            else
            {
                mark[temp]=1;
            }
        }
        printf("Case #%d: %d %d\n",cas++,res1,res2);
    }

    return 0;
}
