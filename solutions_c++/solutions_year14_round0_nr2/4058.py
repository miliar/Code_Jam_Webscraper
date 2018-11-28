#include <iostream>
#include <stdio.h>

using namespace std;
double x,c,f;
bool compromise(double prod_rate);
double fn();

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int cases;
    int p=1;
    scanf("%d",&cases);

    while(cases--)
    {
        cin>>c>>f>>x;
//500.0 4.0 2000.0
        double ans=fn();
        printf("Case #%d: %f\n",p,ans);
        p++;
    }
    return 0;
}

double fn()
{
    if(x<=c)
        return (x/2);

    double prod_rate=2;
    double total_cookies=0;
    double sec=(int)0;

    while(total_cookies<x)
    {
        //printf("in loop \n");
        //printf("rate %f sec %f cook %f \n",prod_rate,sec,total_cookies);


        sec+=(c/prod_rate);
        total_cookies=c;
        if(compromise(prod_rate))
        {
            total_cookies=0;
            prod_rate+=f;
        }
        else
        {
            sec+=(x-total_cookies)/prod_rate;
            break;
        }
    }
    return sec;
}

bool compromise(double prod_rate)
{
    double first=(x-c)/prod_rate;
    double sec=(x)/(prod_rate+f);
    if(sec<first)
        return true;
    return false;
}
