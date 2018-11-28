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
const long long inf = 1e18;

using namespace std;

struct node
{
    int next[ 26 ];
    node()
    {
        for ( int i = 0; i < 26; i++ ) next[i] = -1;
    }
};

int n, m, mx = 0, num = 0, z[ 111 ], h = 0;
string s[ 111 ], cur;
node tree[ 11111 ];

void add( int v, int pos )
{
    if ( pos == cur.size() ) return;
    int c = cur[pos] - 'A';
    if ( tree[v].next[c] == -1 ) tree[v].next[c] = h++;
    add( tree[v].next[c], pos + 1 );  
}

void check()
{
    for ( int i = 0; i < h; i++ ) tree[i] = node();
    h = n;
    for ( int i = 0; i < m; i++ )
    {
        cur = s[i];
        add( z[i], 0 );
    }
    if ( h > mx ) mx = h, num = 0;
    if ( h == mx ) num++;
}

void rec( int pos )
{
    if ( pos == m )
    {
        int msk = 0;
        for ( int i = 0; i < m; i++ ) msk |= ( 1 << z[i] );
        if ( msk + 1 != ( 1 << n ) ) return;
        check();
        return;
    }
    for ( int i = 0; i < n; i++ )
    {
        z[pos] = i;
        rec( pos + 1 );
    }
}

void solve()
{
    mx = 0;
    num = 0;
    cin >> m >> n;
    for ( int i = 0; i < m; i++ ) cin >> s[i];
    rec( 0 );
    cout << mx << " " << num;
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