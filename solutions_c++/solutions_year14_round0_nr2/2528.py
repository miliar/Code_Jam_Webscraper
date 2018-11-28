#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
using namespace std;

double min (double a, double b)
{
       if (a < b)
          return a;
       return b;
}

double solve (int nbBuying,double c, double f, double x, double currentCookie, double rateGainingCookie)
{
        double rs = 0;
        int count = 0;
        while (currentCookie < x)
        {
              currentCookie = c;
              rs += c/rateGainingCookie;
              double t1 = (x-currentCookie)/rateGainingCookie; // Not buying the farm
              if (count < nbBuying)
              {
                 count = count + 1;
                 rateGainingCookie += f;
                 currentCookie = 0;
              }
              else
              {
                  rs += t1;
                  break;
              }
        }
        return rs;
}

int main () {
    ifstream read("input.txt");
    ofstream myfile;
    myfile.open("output.txt");
    myfile.precision (51);
    int t; // Number of test cases
    double c,f,x;
    double currentCookie;
    double rateGainingCookie;
    double rs;
    read >> t;
    for (int z = 0; z < t; z++)
    {
        myfile << "Case #" << (z+1) << ": ";
        read >> c >> f >> x;
        rs = 1000000000;
        for (int tg = 0; tg < 5000; tg++)
        {
            currentCookie = 0;
            rateGainingCookie = 2;
            rs = min (rs, solve (tg, c, f, x, currentCookie, rateGainingCookie));
        }
        myfile << rs;
        myfile << "\n";
    }
    myfile.close();
}
