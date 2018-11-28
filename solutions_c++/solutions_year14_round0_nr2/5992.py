#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Blarge.out","w",stdout);


    int t,cas = 1;

    double C,F,X;

    scanf("%d",&t);

    while(t--){

        scanf("%lf %lf %lf",&C,&F,&X);

        double a = 2,b = X/a,c = C/a,d = 0,time = 0.0;

        while((d+b) > (d + c + (X / (a + F)))){

            d = c;

            a = a + F;
            b = X/a;
            c = C/a;

            time = time + d;
        }
        time = time + b;

        printf("Case #%d: %.7lf\n",cas,time);

        cas++;
    }
    return 0;
}
