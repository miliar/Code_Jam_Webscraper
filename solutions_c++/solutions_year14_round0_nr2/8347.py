#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

int main()
{
    freopen("B-large.in" , "r" , stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    double C,X,F;
    double r=2;

    double T1,T2;

    scanf("%d",&T);
    int stage;

    for(int iter=1;iter<=T;iter++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);

        T1=X/r;
        T2=C/r+X/(r+F);
        stage=1;

        while(T1>T2)
        {
            T1=T2;
            T2=0;
            stage++;
            for(int i=0;i<stage;i++)
            {
                T2+=C/(r+i*F);
            }
            T2+=X/(r+stage*F);
        }

        printf("Case #%d: %0.7lf\n",iter,T1);
    }

    return 0;
}
