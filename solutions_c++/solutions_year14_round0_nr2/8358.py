#include<stdio.h>
int main()
{
    int  t,i,flag;
    double c,f,x,f1,a1,a2,a,ans;
    scanf("%d",&t);

    for(i=1;i<=t;i++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);

       ans=0;
        flag=0;
        if(x>c)
        {

            f1=2.0;


            while(flag!=1)
            {

                a1=x/f1;
                a=c/f1;
                a2=x/(f1+f);

                if(a2+a<a1)
                {
                    ans+=a;
                    f1+=f;
                }
                else
                {
                    ans+=x/f1;
                    flag=1;
                    break;
                }
            }

        }
        else if(x<=c)
        {
            ans=x/2.0;
        }
        printf("Case #%d: %lf\n",i,ans);

    }
    return 0;
}
