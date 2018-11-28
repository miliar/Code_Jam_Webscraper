#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include<iostream>
using namespace std;
bool arr[20];
int main()
{
    freopen("S.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,g;
    double C,F,X,Y;
    scanf("%d",&t);
    g=1;
    while(t--)
    {
        Y=2.0;
        double prev=0.0;
        scanf("%lf %lf %lf",&C,&F,&X);
        while(true)
        {
            double ch1 = (X*1.00/Y*1.00);
            double YY = Y + F;
            double ch2 = (C*1.00/Y*1.00)+(X*1.00/YY*1.00);
            if( ch1<=ch2)
            {
                prev+=ch1*1.00;
                break;
            }
            else
            {
                prev+=(C*1.00/Y*1.00);
                Y=YY;

            }


        }
        printf("Case #%d: %.7lf\n",g++,prev);

    }
}
