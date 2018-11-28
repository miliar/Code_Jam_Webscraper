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
    double c,f,x;
    int n;

    freopen("input.in","r",stdin);
     freopen("out.in","w",stdout);
    scanf("%d", &n);
    for(int i=0; i<n;i++)
    {
        scanf("%lf",&c);
        scanf("%lf",&f);
        scanf("%lf",&x);
        double rate = 2.0;
        double time = 0.0;

        while(1)
        {
            if( (c/rate)+(  x/(rate+f) ) < (x/rate) )
            {
                time += (c/rate);
                rate +=f;
            }
            else
               {
                   time += (x/rate);
                   break;
               }
        }
        printf("Case #%d: %.7f\n",i+1, time);
    }

    return 0;
}
