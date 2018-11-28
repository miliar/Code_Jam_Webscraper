#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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
#define dbg(x) cout << #x << " = " << x << endl
#define dbg2(x,y) cout << #x << " = " << x << ", " << #y << " = " << y << endl
#define rep(i,x,y) for(int i = (x); i < (y); i ++)
#define rep2(i,x,y) for(int i = (x); i <= (y); i ++)
#define dec(i,x,y) for(int i = (x); i >= (y); i --)
#define i64d long long

using namespace std;

int ra, rb;
int a[4][4], b[4][4];

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int nt, idx = 0; scanf("%d", &nt);
    while( (nt --) > 0 ) {
        scanf("%d", &ra); ra --;
        for(int i = 0; i < 4; i ++)
            for(int j = 0; j < 4; j ++)
                scanf("%d", &a[i][j]);
        scanf("%d", &rb); rb --;
        for(int i = 0; i < 4; i ++)
            for(int j = 0; j < 4; j ++)
                scanf("%d", &b[i][j]);
        int res = -1, tot = 0;
        for(int i = 0; i < 4; i ++) {
            for(int j = 0; j < 4; j ++) {
                if( a[ra][i] == b[rb][j] ) {
                    res = a[ra][i];
                    tot ++; break;
                }
            }
        }
        if( tot > 1 )
            printf("Case #%d: Bad magician!\n", ++idx);
        else if( tot == 1 )
            printf("Case #%d: %d\n", ++idx, res);
        else
            printf("Case #%d: Volunteer cheated!\n", ++idx);
    }
    return 0;
}
