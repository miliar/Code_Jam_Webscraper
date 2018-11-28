#include<stdio.h>
int main()
{
    freopen("C:\\Users\\Gaurav\\Desktop\\B1.in","r",stdin);
    freopen("C:\\Users\\Gaurav\\Desktop\\output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int ca=0;
    while(t--)
    {
        ca++;
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double d=2.0;
        int flag=1;
        double ans=0;
        while(flag)
        {
            double a1=x/d;
            double a2=c/d+x/(d+f);
            double g=a2-a1;
            if(g>=0)
            {
                flag=0;
                ans=ans+x/d;
            }
            else
            {
                ans=ans+c/d;
                d=d+f;
            }
        }
        printf("Case #%d: %0.7lf\n",ca,ans);
    }
    return 0;
}
