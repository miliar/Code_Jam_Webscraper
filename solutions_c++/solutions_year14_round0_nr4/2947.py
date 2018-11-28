#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
double a[1001],b[1001];
int mark[1001];
int main()
{
    int ca;
    freopen("F:\\4.in","r", stdin);
	freopen("F:\\4out.txt", "w", stdout);
    scanf("%d",&ca);
    int cc=0;
    while(ca--)
    {
        int n;
        int i,j;
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        scanf("%lf",a+i);
        for(i=1;i<=n;i++)
        scanf("%lf",b+i);

        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        int ans1=0;
        for(i=1;i<=n;i++)
            mark[i]=0;

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            if(b[j]>a[i]&&mark[j]==0)
            {
                ans1++;
                mark[j]=1;
                //st=j+1;
                break;
            }
        }
        int ans2=0;
        for(i=1;i<=n;i++)
            mark[i]=0;
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
            if(a[j]>b[i]&&mark[j]==0)
            {
                ans2++;
                mark[j]=1;
                break;
            }

         printf("Case #%d: %d %d\n",++cc,ans2,n-ans1);
    }
    return 0;
}
            

            
