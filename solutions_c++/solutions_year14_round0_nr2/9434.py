#include <fstream>
#include <stdio.h>

using namespace std;

double solve(double c, double f, double x,double prod)
{
    double timeToFarm = c/prod;
    double timeToX = x/prod;
    double timeToNextX = x/(prod+f);
    if(timeToFarm + timeToNextX < timeToX)
        return timeToFarm + solve(c,f,x,prod+f);
    return timeToX;
}

int main()
{
    unsigned t,i;
    double c,f,x;
    ifstream fin("input.in");
    freopen("output.out","w",stdout);
    fin>>t;
    for(i=1;i<=t;i++)
    {
        fin>>c>>f>>x;
        printf("Case #%d: %.7f\n", i,solve(c,f,x,2.0) );
    }
    return 0;
}
