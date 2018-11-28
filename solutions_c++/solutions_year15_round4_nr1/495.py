#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <memory.h>
#include <cmath>
using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define FOR0(i,n) for( i = 0 ; i < n ; ++i )
#define FOR1(i,n) for( i = 1 ; i <= n ; ++i )
#define sys_p system( "pause" )
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define sz(a) (int)a.size()

typedef long long LL ;

int n, m, r[200][200], b[200][200], x, y, i, j, tr, ans, noans ;
int dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 } ;
char c ;

int main() {
    //ifstream Cin("input.txt");
    freopen("output.txt", "w", stdout);

    int _T, _NT ;
    cin >> _T ;
    for( _NT = 1 ; _NT <= _T ; ++_NT ) {
        cout << "Case #" << _NT << ": " ;

        cin >> n >> m ;
        FOR1(i,n)
            FOR1(j,m) {
                cin >> c ;
                if( c == '.' )
                    r[i][j] = -1 ;
                else if( c == '^' )
                    r[i][j] = 0 ;
                else if( c == '>' )
                    r[i][j] = 1 ;
                else if( c == 'v' )
                    r[i][j] = 2 ;
                else
                    r[i][j] = 3 ;
            }
        ans = 0 ; noans = 0 ;
        FOR1(i,n) {
            if( noans )
                break ;
            FOR1(j, m)
                if (r[i][j] >= 0) {
                    x = j;
                    y = i;
                    while (x > 0 && x <= m && y > 0 && y <= n) {
                        x += dx[r[i][j]];
                        y += dy[r[i][j]];
                        if (r[y][x] >= 0)
                            break;
                    }
                    if (x > 0 && x <= m && y > 0 && y <= n)
                        continue;
                    b[i][j] = 1;

                    FOR0(tr, 4) {
                        x = j;
                        y = i;
                        while (x > 0 && x <= m && y > 0 && y <= n) {
                            x += dx[tr];
                            y += dy[tr];
                            if (r[y][x] >= 0)
                                break;
                        }
                        if (x > 0 && x <= m && y > 0 && y <= n)
                            break;
                    }

                    if (tr < 4)
                        ++ans;
                    else {
                        noans = 1;
                        break;
                    }
                }
        }
        if( noans )
            cout << "IMPOSSIBLE" << endl ;
        else
            cout << ans << endl ;
    }
    return 0 ;
}