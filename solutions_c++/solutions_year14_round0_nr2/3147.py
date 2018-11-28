
#include <iostream>
#include <vector>
#include <limits>

using namespace std;

#define FOR(i,b,e) for(int i=(b); i<=(e); ++i)
#define FORD(i,b,e) for(int i=(b); i>=(e); --i)
#define SIZE(c) (int) c.size()
#define FOREACH(i,c) FOR(i,0,SIZE(c)-1)
#define PB push_back

#define MIN(a,b) ( ((a)<=(b))? (a) : (b) )
#define MAX(a,b) ( ((a)>=(b))? (a) : (b) )

typedef long long int lli;

/************************************************************/

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    cout.precision(7);

    FOR(i,1,t)
    {
        long double c, f, x;
        cin >> c >> f >> x;

        long double k = ( (x * f - 2 * c) / (c * f) );

        long double best = MIN(x / 2 , c / 2 + x / (2 + f));

        long double fork = 0;
        int st = (int) k;

        if (st > 1)
        {
            FOR(j,0,st-1)
                fork += c / (2 + j * f);

            fork += x / (2 + st * f);

            best = MIN(best, fork);
        }

        cout.precision(7);
        cout << "Case #" << i << ": " << fixed << best << endl;
    }



    return 0;
}

/************************************************************/
