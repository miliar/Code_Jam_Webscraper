#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <queue>
#include <stack>

#define sqr(x) (x*x)
#define cube(x) (x*x*x)

using namespace std;

double c,f,x,curr,time,aprox1,aprox2,regen;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i=1; i<=t; i++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        regen=2.0;
        time=0.0;

        while (1)
        {
            aprox1=x/regen;
            aprox2=c/regen;
            aprox2+=(x/(regen+f));

            if (aprox1<=aprox2)
            {
                time+=(x/regen);
                break;
            }
            else
            {
                time+=(c/regen);
                regen+=f;
            }
        }

        printf("Case #%d: %.7lf\n",i,time+1e-8);
    }

    return 0;
}
