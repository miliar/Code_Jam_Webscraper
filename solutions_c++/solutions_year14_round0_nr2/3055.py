#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int number_of_farms(double c, double f, double x)
{
    int n = max(0, static_cast<int>(ceil((x*f - 2*c)/(c*f))) - 1);
    return n;
}

double calc_time(double c, double f, double x, int n)
{
    double resp = x/(2+n*f);
    for(int i=0;i<n;++i)
    {
        resp += c/(2+i*f);
        
    }
    
    return resp;
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int lp=1;lp<=t;++lp)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        auto n = number_of_farms(c, f, x);
        double resp = calc_time(c, f, x, n);
        printf("Case #%d: %.7lf\n", lp, resp);
    }
    return 0;
}