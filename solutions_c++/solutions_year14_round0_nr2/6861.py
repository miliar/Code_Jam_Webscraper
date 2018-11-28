#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <list>

using namespace std;

typedef long long int int64;
typedef long long unsigned int uint64;
typedef unsigned int uint;
#define MAX 4294967290

#define PRINT(x) printf("Case #%d: %.7lf\n", t, x);

unsigned int calsteps(double c, double x, double f)
{
    double left, right, temp=0;
    
    if (((x-c)/2.0) <= (x/(2.0+f))) {
        return 0;
    }

    for(unsigned int i=1; i<MAX; i++) {
        temp += f;
        left = (x-c) / (2.0+temp);
        right = (x) / (2.0+temp+f);
        if (left <= right) {
            return i;
        }
    }
}

double totalSecs(double c, double x, double f, int steps)
{
    double rate = 2.0;
    if (x <= c) return x / rate;
    double secs = c / rate;
    for (int i=1; i<=steps; i++) {
        rate += f;
        secs += c / rate;
    }

    secs += (x-c)/rate;
    return secs;
}

int main()
{
    int tc, s;
    double c, x, f;

    scanf("%d", &tc);
    for(int t=1; t<=tc; t++) {
        scanf("%lf %lf %lf", &c, &f, &x);
        s = calsteps(c, x, f);
        PRINT(totalSecs(c, x, f, s));
    }
    return 0;
}
