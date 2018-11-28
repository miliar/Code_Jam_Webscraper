#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>


using namespace std;

bool megeri(long  gysz, double C, double F, double X)
{
    return (X-C)/(2+gysz*F)>X/(2+F*(gysz+1));
}


int main()
{
     ifstream f("B-large.in");
    ofstream fki("out.txt");
    int t;
    f>>t;
    for (int k=1; k<=t; k++)
    {
         double ido=0.0;
        double C;
        f>>C;
        double F;
        f>>F;
        double X;
        f>>X;
        long gysz=0;
        while (megeri(gysz, C,F,X))
        {
            ido+=C/(gysz*F+2);
            gysz++;
        }
        ido+=X/(gysz*F+2);

        fki<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<ido<<endl;
    }
    return 0;
}
