#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int c,t;
    double a,C,F,X,T,t1,t2,t3;

    cin>>t;
    for(c=0;c<t;c++)
    {
        a=0.0;T=0.0;
        scanf("%lf %lf %lf", &C, &F, &X);
        while(1)
        {
            t1=X/(2.0+a);
            t2=C/(2.0+a);
            t3=(C/(2.0+a)+(X/(2.0+a+F)));
            a=a+F;
            if(t1<t3)
            {
                T=T+t1;
                break;
            }
            else
            {
                T=T+t2;
            }
        }
        printf("Case #%d: %lf\n", c+1, T);
    }
    return 0;
}
