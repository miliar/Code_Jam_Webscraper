#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<math.h>
#include<stdio.h>
#include<stack>
using namespace std;
int main()
{
    freopen("input5.in","r",stdin);
    freopen("o3.txt","w",stdout);
    double t,cost,f,x,rate,i,j,time;
    int k=1;
    cin >> t;
    while(t--)
    {
        rate =2;time=0;
        cin >> cost >> f >> x;
        while(1)
        {
                if((x/rate) >= (cost/rate + x/(rate + f)))
                {
                    time = time + cost/rate;
                    rate = rate + f;
                }
                else if((x/rate) < (cost/rate + x/(rate + f)))
                {
                    time = time + x/rate;
                    break;
                }
        }
        printf("Case #%d: %.8lf\n",k,time);
        k++;
    }

    return 0;
}
