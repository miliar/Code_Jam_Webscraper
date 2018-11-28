#include <fstream>
#include <iomanip>
#include <cmath>
using namespace std;

int n;
double c, f, x, tim;


double timp(double C, double F, double X)
{

    double cpm, farms, money, tt, ti1, tc;
    cpm = 2;
    farms = money = 0;
    tt = X / cpm;

    for (int i = 0; i <= ceil(X / C)+1; ++i)
    {
        cpm = 2;
        ti1 = 0;
        for (int j = 1; j <= i; ++j)
        {
            ti1 += C / cpm;
            cpm += F;
        }
        ti1 += X / cpm;
        if (ti1 < tt)
        {
            tt = ti1;
        }
    }

    return tt;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    fin >> n;
    for (int i = 1; i <= n; ++i)
    {
        fin >> c >> f >> x;
        fout << "Case #" << i << ": " << setprecision(7) << fixed << timp(c, f, x) << "\n";
    }

    return 0;
}