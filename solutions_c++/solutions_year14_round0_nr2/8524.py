#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int testcase,k9=0;
    scanf("%d",&testcase);
    while(testcase--)
    {
        double c9,f9,x9;
        scanf("%lf%lf%lf",&c9,&f9,&x9);
        if(c9>=x9)
        {
            k9++;
        double clock=x9/2;
        printf("Case #%d: %.7lf\n",k9,clock);
       
        }
        else
        {
            k9++;
            double clock=0,r9=2,wi9=0,fi9=0;
            wi9=x9/r9;
            fi9=c9/r9;
            while(1)
            {
                r9=r9+f9;
                if(fi9+x9/r9>wi9)
                {
                    break;
                }
                clock+=fi9;
                fi9=c9/r9;
                wi9=x9/r9;
            }
            clock+=wi9;
            printf("Case #%d: %.7lf\n",k9,clock);
        }
    }
    return 0;
}
