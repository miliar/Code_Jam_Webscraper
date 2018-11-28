
#include <fstream>
#include <iomanip>

using namespace std;

ifstream f1 ("B-large.in");
ofstream f2 ("b.out");

int T;
double C, F, X;

double caz (int x)
{
    double sec, cps;

    f1>>C>>F>>X;

    sec=0;
    cps=2;
    while (X/cps > C/cps + X/(cps+F))
    {
        sec=sec+C/cps;
        cps=cps+F;
    }

    sec=sec+X/cps;

    return sec;

}

int main()
{
    f1>>T;
    f2<<fixed<<setprecision(7);

    for (int i=1; i<=T; i++)
    {
        f2<<"Case #"<<i<<": "<<caz(i)<<endl;
    }

    f1.close();
    f2.close();

    return 0;
}
