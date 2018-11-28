#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int t;
    ifstream fe("B-large.in");
    ofstream fs("B-large.out");
    fe>>t;
    for (int q=1; q<=t; q++)
    {
        double c,f,aux=2;
        double x;
        fe>>c>>f>>x;
        double con=0;
        while ((x/aux)>((x/(aux+f))+(c/aux)))
        {
            con=con+((double)c/(double)aux);
            aux=aux+f;
        }
        con=con+((double)x/(double)aux);
        fs<<"Case #"<<q<<": ";
        fs<<setprecision(7)<<con<<endl;
    }
    return 0;
}
