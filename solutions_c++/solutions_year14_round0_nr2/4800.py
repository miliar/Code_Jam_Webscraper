#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>      // std::setprecision
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORI(i,b) FOR(i,0,b)


int main()
{
    ifstream input("input.in",ifstream::in);
    ofstream output("output.out",ofstream::out);
    output.precision(7);
    int t;
    input >> t;
    FORI(i,t)
    {
        double C,F,X;
        input >> C >> F >> X;
        double res,res1,rate;
        rate = 2.0;
        res1 = X/rate;
        int j = 0;
        do
        {
            res = res1;
            res1 = 0.0;
            rate = 2.0;
            FORI(k,j+1)
            {
                res1+=C/rate;
                rate+=F;
            }
            res1+=X/rate;
            j++;

        }while(res1 < res);
        output.precision(7);
        output << "Case #" << i+1 << ": " << setprecision(15)<<res << endl ;
    }
    return 0;
}
