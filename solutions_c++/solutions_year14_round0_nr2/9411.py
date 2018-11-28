#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

/*
 C - na farmu
 F - přírůstek
 X - konec

30.50000 3.14159 1999.19990

*/

void decide( double &time, double &bestime, double &rate, double c, double f, double x ){

    //cout << time << "  " << bestime << "  " << rate << "  " << c << "  " << f  << "  " << x << "\n";

    time += c/rate;
    if( time >= bestime ) return;

    if( time + x/(rate+f) < bestime ) bestime = time + x/(rate+f);

    rate += f;

    decide( time, bestime, rate, c, f, x );

}

double solve(){

    double c, f, x, rate = 2, time = 0;
    cin >> c >> f >> x;
    double bestime = x/rate;

    decide( time, bestime, rate, c, f, x );

    return bestime;

}


int main()
{
    int p, num = 1;
    cin >> p;

    while( p-- ){

        double s = solve();
        cout << "Case #" << num++ << ": " << std::setprecision(8+log10(s)) << s << "\n";

    }

    return 0;

}


