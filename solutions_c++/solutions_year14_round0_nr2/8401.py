#include<stdio.h>
int main()
{
    int t,k=0;
    scanf("%d",&t);
    while(t--)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        if(c>=x)
        {
            k++;
        double time=x/2;
        printf("Case #%d: %.7lf\n",k,time);
       
        }
        else
        {
            k++;
            double time=0,r=2,wi=0,fi=0;
            wi=x/r;
            fi=c/r;
            while(1)
            {
                r=r+f;
                if(fi+x/r>wi)
                {
                    break;
                }
                time+=fi;
                fi=c/r;
                wi=x/r;
            }
            time+=wi;
            printf("Case #%d: %.7lf\n",k,time);
        }
    }
    return 0;
}