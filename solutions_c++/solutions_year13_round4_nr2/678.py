#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for( int tcase = 1; tcase <= t; ++tcase )
    {
        long long res1, res2, n, p;
        cin >> n >> p;
        long long m = 1;
        for( long long i = 0; i < n; ++i ) m *= 2;
        
        if( p == 1 ) res1 = res2 = 0;
        else if( p == m ) res1 = res2 = m - 1;
        else
        {
            res1 = res2 = 0;
            long long tmp = m / 2, ot = 2, tp = p;
            while( tp > tmp )
            {
                tp -= tmp;
                tmp /= 2;
                res1 += ot;
                ot *= 2;
            }
            
            ot = m / 2, tmp = 1, tp = p;
            while( tp > tmp )
            {
                tp -= tmp;
                tmp *= 2;
                res2 += ot;
                ot /= 2;
            }
        }

        cout << "Case #" << tcase << ": ";
        cout << res1 << ' ' << res2 << endl;
    }
}
