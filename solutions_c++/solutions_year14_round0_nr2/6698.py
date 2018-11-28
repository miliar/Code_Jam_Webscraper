#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    ofstream out("out.txt");
    ifstream in("in.txt");
    int tests=0;
    in >> tests;
    double farmCost=0;
    double farmProduction=0;
    double cookieWanted=0;
    double time=0;
    double prodPerSec;
    double price1=0,price2=0;
    string chaine;
    int j = 0;

    for ( int i = 1 ; i <= tests ; i++ )
    {
        j=0;
        in >> farmCost;
        in >> farmProduction;
        in >> cookieWanted;

        price2=cookieWanted/2.0;
        do
        {
        price1=price2;
        price2-=cookieWanted/(2+j*farmProduction);
        price2+=farmCost/(2+j*farmProduction);
        price2+=cookieWanted/(2+(j+1)*farmProduction);
        j++;
        }
        while(price1>=price2);
        out.precision(49);
        out << "Case #" << i << ": ";
        out << fixed << setprecision (7);
        out << price1 << endl;
    }


    return 0;
}
