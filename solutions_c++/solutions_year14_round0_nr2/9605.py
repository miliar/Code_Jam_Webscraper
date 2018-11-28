#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std ;

double caseSolver(double farmCost, double cookiesPerSecond, double cpsIncrement, double goal)
{
    double time = 0;

    if( (goal/cookiesPerSecond) < ( (farmCost/cookiesPerSecond) + (goal/(cookiesPerSecond+cpsIncrement)) ) )
    {
        time = (goal/cookiesPerSecond) ;
        return time ;
    }
    else
    {
        time = (farmCost/cookiesPerSecond) ;
        cookiesPerSecond += cpsIncrement ;
        return time+( caseSolver(farmCost,cookiesPerSecond,cpsIncrement,goal) ) ;
    }
}

int main ()
{
    ifstream in ("B-small-attempt0.in");
    ofstream out ("output.txt");

    int cases;

    in>>cases;

    for(int k = 0 ; k < cases ; k++)
    {
        double c, f, x ;
        in>>c>>f>>x;
        out<<"Case #"<<k+1<<": "<<setprecision(10)<<caseSolver(c,2,f,x)<<endl;
    }

    return 0 ;
}
