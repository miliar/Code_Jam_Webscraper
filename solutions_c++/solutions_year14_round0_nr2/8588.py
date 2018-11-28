#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;

double farmtime(double C, double F, double productivity)
{
    double rate = 2;
    double time=0;
    while(rate<=productivity)
    {
        time+=C/rate;
        rate+=F;
    }
    return time;
}

int main()
{

    int cases;
    double C,F,X,currentRate,minimum,time;

    //freopen("B-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);

    cin >> cases;
    for(int caseno=1;caseno<=cases;caseno++)
    {
        cin >> C >> F >> X;

        currentRate = 2;
        minimum = X/currentRate;
        time=0;

        while(true)
        {
            time += (C/currentRate);
            if(  minimum > time+(X/(currentRate+F))  )
            {
                minimum = time + (X/(currentRate+F));
            }
            else
            {
                break;
            }
            currentRate+=F;
        }


        printf("Case #%d: %.7lf\n",caseno,minimum);
    }
    return 0;
}

