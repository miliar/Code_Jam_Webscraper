#include<cstdio>
#include<iostream>
 using namespace std;

int main()
{
    int t,k;
    long double c,f,x;
    scanf("%d",&t);
  for( k=1;k<=t;k++)
    {
        scanf("%Lf %Lf %Lf",&c,&f,&x);
        long double r=2.0;
        long double num1=x/r,num2=c/r;
        while(1)
        {

            if(num1 < (num2+ x/(r+f)))
            break;
            else
            {
                num1=num2+x/(r+f);
                num2=num2+c/(r+f);
                r=r+f;
            }
        }
        printf("Case #%d: %0.7Lf\n",k,num1);
    }
return 0;
}
