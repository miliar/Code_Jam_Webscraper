#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    freopen("b_small.in","r",stdin);
    freopen("b_large.txt","w",stdout);
    int times,t;
    scanf("%d",&times);
    for (t = 0; t < times; t++)
    {
        double roi = 2;
        double c,f,x;
        double time = 0;
        scanf("%lf%lf%lf",&c,&f,&x);
        while (true)
        {
            time += c/roi;
            if ((x-c)/roi > x/(roi+f)){
                roi += f;
            }
            else{
                time += (x-c)/roi;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",t+1,time);
    }
}
