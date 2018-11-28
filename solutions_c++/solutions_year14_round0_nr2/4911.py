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
const double EPS = 1e-7;
const lld MOD = 1000000007LL;

int main ( void )
{
    freopen ( "B.in", "r", stdin );
    freopen ( "B-small.txt", "w", stdout );

    cin.sync_with_stdio ( 0 );
    //cout.sync_with_stdio ( 0 );

    int T;
    cin >> T;
    for ( int __T = 1; __T <= T; __T++ )
    {
        double C, F, X;
        cin >> C >> F >> X;

        double currTime = X / 2.;
        double bonusTime = 0;
        double rate = 2.;
        while ( 1 )
        {
            bonusTime += C / rate;
            rate += F;
            if ( currTime < bonusTime + X / rate + EPS ) break;
            currTime = bonusTime + X / rate;
        }
        printf ( "Case #%d: %.7lf\n", __T, currTime );
    }

    return 0;
}
