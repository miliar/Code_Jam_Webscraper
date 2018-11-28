#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const int inf = 1e9;

using namespace std;

int n, a[ 1111 ];
int f[ 1111 ][ 1111 ];
pair< int, int > p[ 1111 ];  

void solve()
{
    cin >> n;
    for ( int i = 1; i <= n; i++ )
    {
        cin >> a[i];
        p[i] = mp( a[i], i );
    }
    sort( p + 1, p + n + 1 );
    for ( int i = 0; i <= n + 1; i++ )
        for ( int j = 0; j <= n + 1; j++ )
            f[i][j] = inf;
    f[0][n + 1] = 0;
    for ( int num = 0; num < n; num++ )
    {
        for ( int i = 0; i <= n; i++ )
        {
            if ( i > num ) break;
            int j = ( n + 1 ) - ( num - i );
            //cout << i << " " << j << " " << f[i][j] << "\n";
            int pos = num + 1;
            int fi = 0, se = 0;
            for ( int k = num + 1; k <= n; k++ )
            {
                if ( p[k].second < p[num].second ) fi++;
                if ( p[k].second > p[num].second ) se++;
            }
            f[i + 1][j] = min( f[i + 1][j], f[i][j] + fi );
            f[i][j - 1] = min( f[i][j - 1], f[i][j] + se );
        }
    }
    int answer = inf;
    for ( int i = 0; i <= n; i++ ) answer = min( answer, f[i][i + 1] );
   // cout << "\n";
    cout << answer;
}

int main (int argc, const char * argv[])
{
    int testcases; cin >> testcases;
    for ( int i = 1; i <= testcases; i++ )
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << "\n";
    }
    return 0;
}