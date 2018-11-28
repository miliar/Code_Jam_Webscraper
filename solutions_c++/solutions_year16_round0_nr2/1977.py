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

char a[maxn];

int main()
{
    srand( time( 0 ) );
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
//    ios_base::sync_with_stdio(false);
    int t;
    scanf ( "%d\n", &t );
    for ( int j = 0; j < t; j++ ){
        gets( a );
        int n = strlen( a );
        for ( int i = 0; i < n; i++ )
            if ( a[i] == '+' )
                a[i] = 1;
            else
                a[i] = 0;
        int ans = 0;
        for ( int i = n - 1; i >= 0; i-- )
            if ( !a[i] ) {
                int l = 0;
                while ( a[l] && l < i )
                    ++l;
                for ( int y = 0; y < l; y++ )
                    a[y] ^= 1;
                if ( l )
                    ++ans;
                for ( int y = 0; y <= i; y++ )
                    a[y] ^= 1;
                reverse( a, a + i + 1 );
                ++ans;
            }
        printf ( "Case #%d: %d\n", j + 1, ans );
    }
    return 0;
}
