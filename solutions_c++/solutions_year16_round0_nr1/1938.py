#include <iostream>
#include <fstream>
#include <list>
#include <stack>
#include <deque>
#include <utility>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <iterator>
#include <cstdio>
#include <cstring>
#include <cstdlib>


using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define f first
#define s second
#define pb push_back
#define mp make_pair

const int maxn = 100500;
const int inf = 2e9;
const double eps = 1e-8;
const int base = 1073676287;

set < int > a;

bool correct( int x ) {
    while ( x ) {
        a.insert( x % 10 );
        x /= 10;
    }
    return a.size() == 10;
}

int main()
{
    srand( time( 0 ) );
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
//    ios_base::sync_with_stdio(false);
    int t;
    scanf ( "%d", &t );
    for ( int j = 0; j < t; j++ ) {
        a.clear();
        int x;
        scanf ( "%d", &x );
        if ( !x ) {
            printf ( "Case #%d: INSOMNIA\n", j + 1 );
            continue;
        }
        int ans = -1;
        for ( int j = 1; j <= 2000; j++ )
            if ( correct( j * x ) ) {
                ans = j;
                break;
            }
        if ( ans != -1 )
            printf ( "Case #%d: %d\n", j + 1, ans * x );
        else
            printf ( "Case #%d: INSOMNIA\n", j + 1 );
    }
    return 0;
}
