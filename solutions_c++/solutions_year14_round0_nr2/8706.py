#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;

int T;

double ret;
double c, f, x;
double curr;
double time;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&T);
    for (int t = 1; t <= T; ++t) {
        fprintf(stderr,"%d\n",t);
        scanf("%lf%lf%lf",&c,&f,&x);

        ret = x / 2.0;

        curr = 2.0;
        time = 0.0;

        while ( time <= ret ) {
            double next = c / curr;
            time += next;
            curr += f;

            double result = time + x / curr;
            if ( result < ret ) ret = result;
        }

        printf("Case #%d: %.7lf\n",t,ret);
    }

    return 0;
}
