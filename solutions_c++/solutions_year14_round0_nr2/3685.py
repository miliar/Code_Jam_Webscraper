#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define inf 2000000000
#define ll long long
#define Max 105

using namespace std;


int main()
{
    double C,F,X;
    int n;

    freopen("input.in","r",stdin);
     freopen("out.in","w",stdout);
    scanf("%d", &n);
    for(int i=0; i<n;i++)
    {
        scanf("%lf",&C);
        scanf("%lf",&F);
        scanf("%lf",&X);
        double rate = 2.0;
        double ti = 0.0;

        while(1)
        {
            if( (C/rate)+(  X/(rate+F) ) < (X/rate) )
            {
                ti += (C/rate);
                rate +=F;
            }
            else
               {
                   ti += (X/rate);
                   break;
               }
        }
        printf("Case #%d: %.7f\n",i+1, ti);
    }

    return 0;
}
