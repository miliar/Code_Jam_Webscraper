#include<cstdio>
int main()
{
    int t,n,a[10000],ans1,ans2,rate;
    scanf("%d",&t);
    for(int j=1;j<=t;j++)
    {
        ans1=0;
        ans2=0;
        rate=0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
        }
        for(int i=2;i<=n;i++)
        {
        if(rate<(a[i-1]-a[i]))
        rate=a[i-1]-a[i];
        }

        for(int i=1;i<n;i++)
        {
            if((a[i]-a[i+1])>0&&i)
            ans1=ans1+(a[i]-a[i+1]);
            if(rate>0)
            {
            if(a[i]>=rate)
            ans2=ans2+rate;
            else
            ans2=ans2+a[i];
            }
            else
            ans2=0;


        }

        printf("Case #%d: %d %d\n",j,ans1,ans2);
    }
    return 0;
}
