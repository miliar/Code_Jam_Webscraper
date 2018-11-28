#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;

int main()
{
    int t,test,k,l;
    float a,b,C,X,d,F,n;
    scanf("%i",&test);
    t=0;
    while(t<test)
    {
                 t++;
                 scanf("%f %f %f",&C,&F,&X);
                 k=1;
                 a=X/2;
                 b=C/2+(X/(F+2));
                 while(a>b)
                 {
                           k++;
                           a=b;
                           b=0;
                           d=2;
                           l=1;
                           while(l<=k)
                           {
                               l++;
                               n=C/d;
                               n=round(n);
                               b=b+n;
                               d=d+F;
                           }
                           b=b+(X/d);
                 }
                 printf("Case #%i: %0.7f\n",t,a);
    }
    return 0;
}
