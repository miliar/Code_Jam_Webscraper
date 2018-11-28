#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    int t,i,j;
    double c,f,x;
    double initialRate,newRate,newRate1,ans[110];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        initialRate = 2.0;
        scanf("%lf %lf %lf",&c,&f,&x);
        newRate = x/initialRate;
        newRate1 = x/initialRate;
        while(1)
        {
            newRate1 = (newRate1 - x/initialRate)+ (c/initialRate) + (x/(initialRate+f));
            initialRate +=f;
            if(newRate1<newRate)
            newRate = newRate1;
            else
            break;
        }
        ans[i]=newRate;
    }
    for(i=1;i<=t;i++)
    {
        printf("Case #%d: %.7lf\n",i,ans[i]);
    }
    return 0;
}
