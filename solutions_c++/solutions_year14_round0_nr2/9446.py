#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

int main()
{

    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,follow;

    scanf("%d",&cases);
    for(int follow=1; follow<=cases; follow++)
    {
        double c,f,x;
        double roof;//=1000000000.000;
        //  printf("%lf",roof);
        scanf("%lf %lf %lf",&c,&f,&x);

        if(c>=x)
            printf("Case #%d: %0.7lf\n",follow,x/2);
        else
        {
            roof=x/2.0;
            double sum=(c/2.0)+(x/(2.0+f)),sum1=c/2.0;
            if(sum<roof)
            {
                roof=sum;
                for(double i=2.0+f;; i=i+f)
                {
                    sum1=sum1+(c/i)+(x/(i+f));
                    if(sum1<roof)
                    {
                        roof=sum1;
                        sum1=sum1-(x/(i+f));
                    }
                    else
                        break;


                }
                printf("Case #%d: %0.7lf\n",follow,roof);

            }
            else
             printf("Case #%d: %0.7lf\n",follow,roof);
        }
}

return 0;
}
