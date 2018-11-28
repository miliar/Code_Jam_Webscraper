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


int main()
{
    srand( time( 0 ) );
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
//    ios_base::sync_with_stdio(false);
    int t;
    scanf ( "%d", &t );
    for ( int j = 0; j < t; j++ ) {
        int k, c, s;
        scanf ( "%d%d%d", &k, &c, &s );
        printf ( "Case #%d: ", j + 1 );
        ll cnt = 1LL;
        for ( int i = 1; i < c; i++ )
            cnt *= 1LL * k;
        if ( c == 1 )
            cnt = 0LL;
        ll cur = 0LL;
        for ( int i = 1; i <= k; i++ ) {
            cout << cur + 1LL * i << ' ';
            cur += cnt;
        }
        cout << endl;
    }
    return 0;
}
