#include<cstdio>
#include<cmath>
#include<cstdlib>

int main()
{
    int test;
    scanf("%d",&test);

    for(int t=0;t<test;t++)
    {
        double c,f,x,rate,textra,tbuy;
        scanf("%lf%lf%lf",&c,&f,&x);

        rate=2.0;
        textra=(x/rate);
        double totalbuy=0.0;
        while(1)
        {
            tbuy=c/rate;
            totalbuy+=tbuy;
            rate+=f;

            double tnew=(x/rate)+totalbuy;

            if(tnew>textra)
            {
                printf("Case #%d: %lf\n",t+1,textra);
                break;
            }
            else
            {
                textra=tnew;
            }
        }
    }
    return 0;
}
