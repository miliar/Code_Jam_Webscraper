#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int t,n,i,x=1,cnt=0,j;
    scanf("%d",&t);
    while(t--)
    {
        cin>>n;
        double a[n];
        double b[n];
        double d[n];
        int c[n];
        for(i=0;i<n;i++)
        {
            scanf("%lf",&a[i]);
            c[i]=0;
        }
         for(i=0;i<n;i++)
        {
            scanf("%lf",&b[i]);
        }
        sort(a,a+n);
        sort(b,b+n);
         for(i=0;i<n;i++)
        {
            d[i]=b[i];
        }
        int flag=0;
        cnt=0;
        for(i=0;i<n;i++)
        {   flag=0;
            for(j=0;j<n;j++)
            {
                if(d[j]>a[i])
                {
                    d[j]=0;
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                cnt++;
                for(j=0;j<n;j++)
                {
                    if(d[j]!=0)
                    {
                        d[j]=0;
                    }
                }
            }
        }
        int cnt1=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(a[j]>b[i])
                {
                    a[j]=0;
                    cnt1++;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",x++,cnt1,cnt);
    }
}
