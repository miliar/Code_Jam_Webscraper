#include <fstream>
#include <iostream>
#include <iomanip>

#define inf 999999999
using namespace std;
ifstream f("inputb.txt");
ofstream g("b.txt");

int t;
double C,F,X;
double sol1,sol2,solmin;
double profit ;
double time;

int main()
{
    f >> t;
     for (int k = 1; k <= t ; k++)
     {
        f >> C >> F >> X;
        sol1 = 0; sol2 = 1; solmin = inf; time = 0;
            profit = 2;
         cout.precision(7);
        while (sol1 < sol2)
        {
        sol2  = (X / profit) + time;
        sol1 = (C / profit) + (X / (profit + F)) + time;

        if (sol1 < sol2)
        {
            solmin = sol1;
            time += (C/profit);
            profit += F;
        }
            else  if (sol2 < solmin) solmin = sol2;

        }

        g << "Case #" << k<<": " <<fixed << setprecision(7) << solmin << '\n';
     }


    return 0;
}
