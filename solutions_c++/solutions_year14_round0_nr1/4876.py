/*
    Aleksandar "Al3kSaNdaR" Ivanović

    Problem A. Magic Trick
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

int T, row1, row2, X, Row1[17], Row2[17];
vector < int > Sol;

int main ( void )
{
    freopen ( "A.in", "r", stdin );
    freopen ( "A.txt", "w", stdout );

    cin.sync_with_stdio ( 0 );
    cout.sync_with_stdio ( 0 );

    cin >> T;
    for ( int __T = 1; __T <= T; __T++ )
    {
        cin >> row1;
        for ( int i = 1; i <= 4; i++ )
            for ( int j = 1; j <= 4; j++ ) cin >> X, Row1[X] = i;
        cin >> row2;
        for ( int i = 1; i <= 4; i++ )
            for ( int j = 1; j <= 4; j++ ) cin >> X, Row2[X] = i;

        Sol.clear ( );
        for ( int i = 1; i <= 16; i++ ) if ( Row1[i] == row1 && Row2[i] == row2 ) Sol.pb ( i );

        cout << "Case #" << __T << ": ";
        if ( Sol.empty ( ) ) cout << "Volunteer cheated!" << endl;
        else if ( Sol.size ( ) > 1 ) cout << "Bad magician!" << endl;
             else cout << Sol[0] << endl;
    }

    return 0;
}
