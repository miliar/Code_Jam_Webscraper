#include <iostream>
#include <iomanip>

using namespace std;

double prox_t( double vi, double c, double f, double x, double aT, double pT)
{
    return (aT < pT)? aT : prox_t(vi+f, c, f, x, pT, (pT-(x/vi))+(c/vi)+(x/(vi+f)) );
}


int main()
{
    int i(0);
    double t, vi(2), c, f, x, pT, aT;
    cin >> t;
    while(t--)
    {
        cin >> c >> f >> x;
        cin.ignore();

        aT = x/vi;
        pT = (c/vi) + (x/(vi+f));

        cout << fixed << setprecision(7) << "Case #" << ++i << ": " << prox_t(vi+f, c, f, x, aT, pT) << endl;
    }

    return 0;
}
