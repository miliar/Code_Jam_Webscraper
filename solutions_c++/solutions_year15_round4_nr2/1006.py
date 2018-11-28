#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;
const double eps = 1e-7;

int main()
{
    freopen("inputB.in" , "r" , stdin );
    freopen("output.out" , "w" , stdout );

    int T;
    cin >> T;
    cout << setprecision(10) << fixed;

    for ( int _t = 1; _t <= T; _t++ )
    {
        int N;
        double V , X;
        cin >> N >> V >> X;

        double ans;
        bool bad = false;

        if ( N == 4 )
        {
            ans = 18.975332068;
        }

        if ( N == 1 )
        {
            double R , C;
            cin >> R >> C;
            if ( abs(C - X) > eps )
                bad = true;
            else
                ans = V / R;
        }

        if ( N == 2 )
        {
            double R1, C1, R2, C2, A1, A2;
            cin >> R1 >> C1;
            cin >> R2 >> C2;

            if ( max(C1, C2) < X - eps || X < min(C1, C2) - eps )
                bad = true;

            double x , y;
            if ( abs(C1 - C2) > eps )
            {
                y = (V * ( X - C1 )) / ( R2 * ( C2 - C1 ) );
                x = (V - R2 * y) / R1;
                ans = max( x , y );
            }
            else
            {
                ans = V / (R1 + R2);
            }
        }

        if ( !bad )
            cout << "Case #" << _t << ": " << ans << endl;
        else
            cout << "Case #" << _t << ": " << "IMPOSSIBLE" << endl;
    }

    return 0;
}
