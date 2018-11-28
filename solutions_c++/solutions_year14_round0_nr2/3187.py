#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1200000
#define EPS 1e-7

using namespace std;

double C,F,X;

double memo[MAX + 100];

double f()
{    
    FORD(factory,MAX,0)
    {
        double duration = X / (F * (double)factory + 2);
        if(factory == MAX) memo[factory] = duration;
        else
        {
            double duration2 = C / (F * (double)factory + 2);
            memo[factory] = min(duration,memo[factory + 1] + duration2);   
        }        
    }
    return memo[0];
    /*
    double duration = X / (F * (double)factory + 2);
    if(duration <= 1) return duration;
    double duration2 = C / (F * (double)factory + 2);
    return min(duration,f(factory + 1) + duration2);*/
}

double solve(int ca)
{
    scanf("%lf %lf %lf",&C,&F,&X);
    printf("Case #%d: %.7lf\n",ca,f());
}

int main()
{
    int t;
    scanf("%d",&t);
    FOR(ca,1,t)
    {
        solve(ca);
    }
    return 0;
}
