#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int T;
    double C, F, X, rez, lRez;

    freopen( "qualB.in", "r", stdin );
    freopen( "qualB.out", "w", stdout);

    cin >> T;

    for( int t=0; t<T; t++ )
    {
        cout << "Case #" << t+1 << ": ";
        cin >> C >> F >> X;

        rez = X/2;
        lRez = X;

        for( int i=1; lRez > rez; i++ )
        {
            lRez = rez;
            rez += X/( 2 + F*i ) - X/( 2 + F*(i-1) ) + C/( 2 + F*(i-1) );
        }

        cout << fixed << std::setprecision(7) << lRez << endl;
    }
}
