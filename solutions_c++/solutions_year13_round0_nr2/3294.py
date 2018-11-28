#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 110;
int T;
int g[N][N], maze[N][N];
int col[N], row[N];

int main()
{
    freopen("l.in", "r", stdin);
    freopen("lp.txt", "w", stdout);

    scanf("%d", &T);
    int icase = 1;
    while ( T-- ) {
        memset( col, 0, sizeof(col) );
        memset( row, 0, sizeof(row) );
        int n, m;
        bool is = true;
        scanf("%d%d", &n, &m);
        for ( int i = 0; i < n; ++i )
            for ( int j = 0; j < m; ++j ) {
                scanf("%d", &maze[i][j]);
                if ( maze[i][j] > col[j] ) col[j] = maze[i][j];
                if ( maze[i][j] > row[i] ) row[i] = maze[i][j];
                g[i][j] = 100;
            }
        for ( int i = 0; i < n; ++i )  
            for ( int j = 0; j < m; ++j ) 
                if ( g[i][j] != maze[i][j] ) {
                    int k;
                    if ( maze[i][j] == row[i] ) { 
                        for ( k = 0; k < m; ++k ) if( g[i][k] > row[i] ) g[i][k] = row[i];
                        //cout << i << ' ' << j << g[i][k] << row[i] << endl;
                    }
                    else if ( maze[i][j] == col[j] ){
                        for ( k = 0; k < n; ++k ) if( g[k][j] > col[j] ) g[k][j] = col[j];
                        //cout << i << ' ' << j << g[i][k] << col[j] << endl;
                    }
                }
       //for ( int i = 0; i < n; ++i, cout << endl ) for ( int j = 0; j < m; ++j ) cout << g[i][j] << " ";
       //for ( int i = 0; i < n; ++i ) cout << row[i] << " ";
       //for ( int j = 0; j < m; ++j ) cout << col[j] << " ";
        for ( int i = 0; i < n; ++i ) for ( int j = 0; j < m; ++j ) if ( maze[i][j] != g[i][j] ) {
            is = false;
            break;
        }
        printf("Case #%d: ", icase++);
        if ( is ) printf("YES\n");
        else printf("NO\n");
    }
}
