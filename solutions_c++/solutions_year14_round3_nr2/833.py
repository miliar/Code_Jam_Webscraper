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

const int maxN = 10 + 2;

int n;
char str[maxN][maxN * maxN];
char dst[maxN * maxN * maxN];
int num[maxN];
bool vst[128];

bool chk()
{
    memset(vst, 0, sizeof(vst));
    int len = strlen(dst);
    for(int i = 0; i < len; ) {
        if( vst[ dst[i] ] )
            return false;
        vst[ dst[i] ] = true;
        int j;
        for(j = i + 1; j < len; j ++) {
            if( dst[j] == dst[i] )
                continue;
            else
                break;
        }
        i = j;
    }
    //puts(dst);
    return true;
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int nt, idx = 0;
    scanf("%d", &nt);
    for(; nt > 0; nt --) {
        scanf("%d", &n);
        for(int i = 0; i < n; i ++)
            scanf("%s", str[i]);
        for(int i = 0; i < n; i ++)
            num[i] = i;
        int res = 0;
        do {
            int n_dst = 0;
            for(int i = 0; i < n; i ++) {
                strcpy(dst + n_dst, str[ num[i] ]);
                n_dst += strlen( str[ num[i] ] );
            }
            if( chk() )
                res ++;
        } while( next_permutation(num, num + n) );
        printf("Case #%d: %d\n", ++idx, res);
    }
    return 0;
}
