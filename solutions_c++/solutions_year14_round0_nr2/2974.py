/*
Author:BobLee
Email:BobLee0717@gmail.com
*/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<vector>
using namespace std;

double c,f,x;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int t;
    cin>>t;
    int ca=1;
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double have = 0;
        double seconds = 0;
        double speed=2;
        while(have<x)
        {
            if(have>=c)
            {
                if( ((x-have)/speed) < ((x-have+c)/(speed+f)) )
                {
                    seconds += ((x-have)/speed);
                    break;
                }
                else
                {
                    speed += f;
                    have -=c;
                }
            }
            else
            {
                if( ((x-have)/speed) < ( (c-have)/speed ) )
                {
                    seconds+=((x-have)/speed);
                    break;
                }
                seconds+= (c-have)/speed;
                have = c;
            }
        }

        printf("Case #%d: %.8lf\n",ca++,seconds);

    }
    return 0;
}
