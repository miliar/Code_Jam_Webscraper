#include <iostream>
#include <fstream>
#include <locale>
#include <cmath>
#include <sstream>
using namespace std;

main()
{
    ifstream infile("A.in");
    ofstream outfile("A.out");
    int i, j, k;
    int n, t;
    long double rad1, rad2 = 0;
    long double paint;
    long double paint_took;
    long double pie = 3.14;
    int rings;
    bool first;

    //Get number of test cases
    infile >> t;

    for(i=0;i<t;i++)
    {
        outfile << "Case #" << i+1 << ": ";
        first = true;
        paint = 0;
        rings = 0;

        while(paint >=0)
        {
            //First time
            if(first)
            {
                infile >> rad1;
                infile >> paint;
                first = false;
            }

            //Circle we draw is larger than the measeure by 1 cm
            rad2 = rad1 + 1;

            paint_took = (rad2 * rad2) - (rad1 * rad1);
            paint = paint - paint_took;

            if(paint >= 0);
            {
                rings = rings + 1;
            }

            rad1 = rad2 + 1;
        }

        outfile << rings-1 << endl;
    }


}
