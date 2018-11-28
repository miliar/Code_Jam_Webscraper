/*
    Aleksandar "Al3kSaNdaR" Ivanović
*/
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <bitset>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <utility>
#include <functional>

#define pb push_back
#define mp make_pair
#define sz size
#define all(X) (X).begin(), (X).end ()
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)

using namespace std;

typedef long long int lld;
typedef pair < int, int > pii;

const int INF = 1 << 30;
const double EPS = 1e-9;
const lld MOD = 1000000007LL;

const int MaxN = 1 << 10;

int t, n;
double naomi[MaxN], ken[MaxN];


int main ( void )
{
    //freopen ( "D-small-attempt0.in", "r", stdin );
    //freopen ( "D-small-attempt0.out", "w", stdout );

    freopen ( "D-large.in", "r", stdin );
    freopen ( "D-large.out", "w", stdout );

    cin.sync_with_stdio ( 0 );
    cout.sync_with_stdio ( 0 );

    cin >> t;
    for ( int __t = 1; __t <= t; __t++ )
    {
        cin >> n;
        for ( int i = 0; i < n; i++ ) cin >> naomi[i];
        for ( int i = 0; i < n; i++ ) cin >> ken[i];

        sort ( naomi, naomi + n );
        sort ( ken, ken + n );

        int idy = 0, pointsWar = 0;
        for ( int idx = 0; idx < n; idx++ )
        {
            while ( idy < n && ken[idy] < naomi[idx] ) idy++;
            if ( idy == n ) pointsWar++;
            else idy++;
        }

        int left = 0, right = n - 1, pointsDeceitfulWar = 0;
        for ( int i = 0; i < n; i++ )
        {
            if ( naomi[i] < ken[left] && naomi[i] < ken[right] ) right--;
            else
            {
                pointsDeceitfulWar++;
                if ( naomi[i] > ken[right] ) right--;
                else left++;
            }
        }


        cout << "Case #" << __t << ": " << pointsDeceitfulWar << " " << pointsWar << endl;
    }

    return 0;
}
