#include<cstdio>
#include<iostream>

using namespace std;
int main()
{
    double c,f,x,total,m,z,a1,a2,a3;
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        total=0;

        scanf("%lf%lf%lf",&c,&f,&x);
        m=2.0;
        for(;;)
        {
            a1=x/m;
            a2=c/m;
            a3=x/(m+f);
            if(a1<(a2+a3))
                break;

            z=c/m;
            total=total+z;

             m=m+f;

        }
        total=total+(x/m);

        printf("Case #%d: %.7lf \n",i,total);

    }
return 0;
}
