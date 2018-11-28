#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
using namespace std;
double a[1010];
double b[1010];
//bool fg[1010];
bool cmp(double x,double y)
{
    return x<y;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    int ncase;
    int T=0;
    scanf("%d",&ncase);
    while(ncase--)
    {
        int n,i,j;
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
        //memset(fg,false,sizeof(fg));
        sort(a,a+n,cmp);
        sort(b,b+n,cmp);
        j=0;
        int ans2=n,ans1=0;
        for(i=0;i<n;i++)
        {
            for(;j<n;j++)
            {
                if(b[j]>a[i])
                {
                    ans2--;
                    j++;
                    break;
                }
            }
        }
        int num=0;
        for(i=0;i<n;i++)
        {
            if(a[i]>b[num])
            {
                ans1++;
                num++;
            }

        }
        printf("Case #%d: %d %d\n",++T,ans1,ans2);
    }
    return 0;
}
