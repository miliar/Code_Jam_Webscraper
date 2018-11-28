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

struct rect
{
    int a, b, c, d;
    rect( int a = 0, int b = 0, int c = 0, int d = 0 ) : a( a ), b( b ), c( c ), d( d ) {};
};

struct edge
{
    int v, c, f;
    edge( int v = 0, int c = 0, int f = 0 ) : v( v ), c( c ), f( f ) {}; 
};

int dx[ 2 ] = { 0, 1 };
int dy[ 2 ] = { 1, 0 };
rect rr[ 1111 ];
vector< edge > e;
vector< int > graph[ 2 * 111 * 555 ];
int n, m, k, h, S, T;
int id_x[ 111 ], id_y[ 555 ];
bool field[ 111 ][ 555 ];
int fi[ 111 ][ 555 ], se[ 111 ][ 555 ];
int d[ 2 * 111 * 555 ], p[ 2 * 111 * 555 ];

void add_edge( int v, int u, int c )
{
    graph[v].push_back( e.size() );
    e.push_back( edge( u, c, 0 ) );
    graph[u].push_back( e.size() );
    e.push_back( edge( v, 0, 0 ) );
}

void bfs()
{
    for ( int i = S; i <= T; i++ )
    {
        d[i] = -1;
        p[i] = 0;
    }
    d[S] = 0;
    queue< int > q; q.push( S );
    while ( q.size() )
    {
        int v = q.front(); q.pop();
        for ( int i = 0; i < graph[v].size(); i++ )
        {
            int id = graph[v][i];
            if ( e[id].c - e[id].f == 0 ) continue;
            int next = e[id].v;
            if ( d[ next ] != -1 ) continue;
            d[ next ] = d[v] + 1;
            q.push( next );
        }
    }
}

int dfs( int v, int flow )
{
    if ( v == T ) return flow;
    if ( flow == 0 ) return 0;
    int pushed = 0;
    for ( ; p[v] < graph[v].size(); p[v]++ )
    {
        int id = graph[v][ p[v] ];
        if ( e[id].c - e[id].f == 0 ) continue;
        int next = e[id].v;
        if ( d[v] + 1 != d[ next ] ) continue;
        int delta = dfs( next, min( flow - pushed, e[id].c - e[id].f ) );
        e[ id ].f += delta;
        e[ id ^ 1 ].f -= delta;
        pushed += delta;
        if ( pushed == flow ) return pushed;  
    }
    return pushed;
}

void solve()
{
    cin >> n >> m >> k;
    //set< int > yy;
    for ( int i = 0; i < k; i++ ) 
    {
        cin >> rr[i].a >> rr[i].b >> rr[i].c >> rr[i].d;
        /*xx.insert( rr[i].a );
        if ( rr[i].a + 1 < n )  xx.insert( rr[i].a + 1 );
        if ( rr[i].a - 1 >= 0 ) xx.insert( rr[i].a - 1 );
        //-----------------
        yy.insert( rr[i].b );
        if ( rr[i].b + 1 < m )  yy.insert( rr[i].b + 1 );
        if ( rr[i].b - 1 >= 0 ) yy.insert( rr[i].b - 1 );
        //-----------------
        xx.insert( rr[i].c );
        if ( rr[i].c + 1 < n )  xx.insert( rr[i].c + 1 );
        if ( rr[i].c - 1 >= 0 ) xx.insert( rr[i].c - 1 );
        //-----------------
        yy.insert( rr[i].d );
        if ( rr[i].d + 1 < m )  yy.insert( rr[i].d + 1 );
        if ( rr[i].d - 1 >= 0 ) yy.insert( rr[i].d - 1 );*/
    }
    //int hx = n, hy = m;
    //for ( set< int >::iterator it = xx.begin(); it != xx.end(); it++ ) id_x[ *it ] = hx++;
    //for ( set< int >::iterator it = yy.begin(); it != yy.end(); it++ ) id_y[ *it ] = hy++;
    //n = hx;
    //m = hy;
    //cout << n << " " << m << "\n";
    for ( int i = 0; i < n; i++ )
        for ( int j = 0; j < m; j++ )
            field[i][j] = false;
    for ( int i = 0; i < k; i++ )
    {
        //rr[i].a = id_x[ rr[i].a ];
        //rr[i].b = id_y[ rr[i].b ];
        //rr[i].c = id_x[ rr[i].c ];
        //rr[i].d = id_y[ rr[i].d ];
        for ( int x = rr[i].a; x <= rr[i].c; x++ )
            for ( int y = rr[i].b; y <= rr[i].d; y++ )
                field[x][y] = true;
    }
    /*for ( int i = 0; i < n; i++ )
    {
        for ( int j = 0; j < m; j++ ) cout << field[i][j];
        cout << "\n";
    }*/
    S = 0;
    int h = 1;
    for ( int i = 0; i < n; i++ )
        for ( int j = 0; j < m; j++ )
        {
            fi[i][j] = h++;
            se[i][j] = h++;
        }
    T = h;
    //----------------------------
    e.clear();
    for ( int i = S; i <= T; i++ ) graph[i].clear();
    for ( int i = 0; i < n; i++ )
        for ( int j = 0; j < m; j++ )
            add_edge( fi[i][j], se[i][j], !field[i][j] );
    for ( int i = 0; i < n; i++ ) 
    {
        add_edge( S, fi[i][0], 1 );
            add_edge( se[i][m - 1], T, 1 );
    }
    for ( int i = 0; i < n; i++ )
        for ( int j = 0; j < m; j++ )
            for ( int k = 0; k < 2; k++ )
            {
                int _i = i + dx[k];
                int _j = j + dy[k];
                if ( _i == n ) continue;
                if ( _j == m ) continue;
                add_edge( se[i][j], fi[_i][_j], 1 );
                add_edge( se[_i][_j], fi[i][j], 1 );
            }
    int flow = 0;
    while ( true )
    {
        bfs();
        if ( d[T] == -1 ) break;
        while ( true )
        {
            int pls = dfs( S, 1000000000 );
            if ( pls == 0 ) break;
            flow += pls; 
        }
    }
    cout << flow;
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