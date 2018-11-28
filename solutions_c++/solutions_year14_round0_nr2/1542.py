#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)

using namespace std;

int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);

    int t;
    double c, f, x, v;
    double time;

    scanf("%d", &t);
    for(int ncaso=1; ncaso<=t; ncaso++)
    {
        scanf("%lf %lf %lf", &c, &f, &x);

        v = 2.0;
        time = 0.0;

        while(x/v > (c/v) + (x/(v+f)))
        {
            time += c/v;
            v = v+f;
        }

        time += x/v;

        printf("Case #%d: %.7f\n", ncaso, time);
    }

    return 0;
}
