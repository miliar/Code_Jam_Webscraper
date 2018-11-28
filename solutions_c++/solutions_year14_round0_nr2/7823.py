#include<stdio.h>
#include<math.h>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    for(int w=1;w<=t;w++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);

        double z=((x*f)/c -2)/f -1;
        int z1=ceil(z),j;
        double ans,k1,k2;

        if(z1>0)
        {
            ans=(x)/(2+ z1*f);
            for(k1=2,j=0;j<z1;j++)
            {
                ans+=c/k1;
                k1+=f;
            }


        }
        else ans=x/2.0;

        printf("Case #%d: %.7f\n",w,ans);


    }
}
