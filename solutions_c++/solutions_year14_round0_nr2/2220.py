#include<stdio.h>
#include<string.h>
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cnt=0;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        printf("Case #%d: ",++cnt);
        if(x<=c)
        {
            printf("%.7lf\n",x/2);
        }
        else
        {
            double g=2;
            double res=0;
            int flag=1;
            while(flag)
            {
                double a=x/g;
                double b=c/g+x/(g+f);
                //printf("**%.7lf\n",a);
                if(a<b)
                    res+=a,flag=0;
                else
                    res+=c/g,g+=f;
            }
            printf("%.7lf\n",res);
        }
    }
    return 0;
}
