#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
//#define _LOCAL_
#ifdef _LOCAL_
#include "testlib.h"
/* rnd */
#endif

using namespace std;

#define dbg(x) cout << #x << " = " << (x) << endl
#define dbg2(x,y) cout << #x << " = " << (x) << ", " << #y << " = " << (y) << endl
#define dbg3(x,y,z) cout << #x << " = " << (x) << ", " << #y << " = " << (y) << ", " << #z << " = " << (z) << endl

template<class T> inline T cabs(T x) { return x > 0 ? x : (-x); }
template<class T> inline T gcd(T x, T y) { return (y == 0) ? x : gcd(y, x % y); }

#define out(x) cout << (x) << endl
#define out2(x,y) cout << (x) << " " << (y) << endl
#define out3(x,y,z) cout << (x) << " " << (y) << " " << (z) << endl

const int maxN = 100 + 10;

int R, C;
char str[maxN][maxN];
int vst[maxN][maxN];

int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
int isOK(int x, int y) { return x >= 0 && x < R && y >= 0 && y < C; }

int get_val(char ch)
{
    if( ch == '^' ) return 3;
    if( ch == '>' ) return 0;
    if( ch == 'v' ) return 2;
    return 1;
}

int cnt;

int dfs(int x, int y, char ch)
{
    if( !isOK(x, y) )
        return 0;
    if( vst[x][y] )
        return 1;
    if( str[x][y] == '.' ) {
        int val = get_val(ch);
        return dfs(x + dir[val][0], y + dir[val][1], ch);
    } else {
        int val = get_val(str[x][y]), tid;
        vst[x][y] = 1;
        if( dfs(x + dir[val][0], y + dir[val][1], str[x][y]) )
            return 1;
        vst[x][y] = 0;

        if( str[x][y] != '^' ) {
            char tmp = str[x][y];
            str[x][y] = '^';
            vst[x][y] = 1; cnt ++;
            tid = get_val('^');
            if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
                return 1;
            str[x][y] = tmp;
            vst[x][y] = 0; cnt --;
        }

        if( str[x][y] != '>' ) {
            char tmp = str[x][y];
            str[x][y] = '>';
            vst[x][y] = 1; cnt ++;
            tid = get_val('>');
            if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
                return 1;
            str[x][y] = tmp;
            vst[x][y] = 0; cnt --;
        }

        if( str[x][y] != 'v' ) {
            char tmp = str[x][y];
            str[x][y] = 'v';
            vst[x][y] = 1; cnt ++;
            tid = get_val('v');
            if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
                return 1;
            str[x][y] = tmp;
            vst[x][y] = 0; cnt --;
        }

        if( str[x][y] != '<' ) {
            char tmp = str[x][y];
            str[x][y] = '<';
            vst[x][y] = 1; cnt ++;
            tid = get_val('<');
            if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
                return 1;
            str[x][y] = tmp;
            vst[x][y] = 0; cnt --;
        }

        return 0;
    }
}

int run(int x, int y)
{
    if( vst[x][y] )
        return 0;
    if( str[x][y] == '.' )
        return 0;

    cnt = 0;

    int tid = get_val(str[x][y]);
    vst[x][y] = 1;
    if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
        return cnt;
    vst[x][y] = 0;

    if( str[x][y] != '^' ) {
        char tmp = str[x][y];
        str[x][y] = '^';
        vst[x][y] = 1;
        tid = get_val('^');
        if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
            return 1 + cnt;
        str[x][y] = tmp;
        vst[x][y] = 0;
    }

    if( str[x][y] != '>' ) {
        char tmp = str[x][y];
        str[x][y] = '>';
        vst[x][y] = 1;
        tid = get_val('>');
        if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
            return 1 + cnt;
        str[x][y] = tmp;
        vst[x][y] = 0;
    }

    if( str[x][y] != 'v' ) {
        char tmp = str[x][y];
        str[x][y] = 'v';
        vst[x][y] = 1;
        tid = get_val('v');
        if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
            return 1 + cnt;
        str[x][y] = tmp;
        vst[x][y] = 0;
    }

    if( str[x][y] != '<' ) {
        char tmp = str[x][y];
        str[x][y] = '<';
        vst[x][y] = 1;
        tid = get_val('<');
        if( dfs(x + dir[tid][0], y + dir[tid][1], str[x][y]) )
            return 1 + cnt;
        str[x][y] = tmp;
        vst[x][y] = 0;
    }


    return -1;
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int idx = 0, nt;
    scanf("%d", &nt);
    for(; nt > 0; nt --) {
        scanf("%d %d", &R, &C);
        for(int i = 0; i < R; i ++)
            scanf("%s", str[i]);
        int res = 0;
        memset(vst, 0, sizeof(vst));
        for(int i = 0, j, k; res >= 0 && i < R; i ++)
            for(j = 0; res >= 0 && j < C; j ++) {
                k = run(i, j);
                //dbg3(i, j, k);
                if( k == -1 )
                    res = -1;
                else
                    res += k;
            }
        if( res == -1 )
            printf("Case #%d: IMPOSSIBLE\n", ++ idx);
        else
            printf("Case #%d: %d\n", ++ idx, res);
    }
    return 0;
}
