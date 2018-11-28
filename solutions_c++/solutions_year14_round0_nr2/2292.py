#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
     freopen("ans2.txt","w",stdout);
    freopen("B-small-attempt2.in","r",stdin);
    int t,k;
    double c,f,x;
    scanf("%d",&t);
  for( k=1;k<=t;k++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        double num=2.0,temp;
          double num1=x/num,num2=c/num;
        while(1)
        {
            num=num+f;
temp=num2+x/num;
            if(num1 <temp)
            break;
            else
            {
                //num=num+f;
                num1=temp;
                num2=num2+c/(num);
               
            }
        }
        printf("Case #%d: %.7lf\n",k,num1);
    }
return 0;
}
