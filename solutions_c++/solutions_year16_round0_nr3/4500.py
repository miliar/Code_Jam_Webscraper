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
#include <fstream>

using namespace std;

template<class T> inline T cabs(const T &x) { return x > 0 ? x : (-x); }
template<class T> inline T gcd(const T &x, const T &y) { return (y == 0) ? x : gcd(y, x % y); }
template<class T> inline T sgn(const T &x) { return (x > 0) - (x < 0); }

#define dbg(x) cout << #x << " = " << (x) << endl
#define dbg2(x,y) cout << #x << " = " << (x) << ", " << #y << " = " << (y) << endl
#define dbg3(x,y,z) cout << #x << " = " << (x) << ", " << #y << " = " << (y) << ", " << #z << " = " << (z) << endl
#define dbg4(x,y,z,w) cout << #x << " = " << (x) << ", " << #y << " = " << (y) << ", " << #z << " = " << (z) << ", " << #w << " = " << w << endl

#define out(x) cout << (x) << endl
#define out2(x,y) cout << (x) << " " << (y) << endl
#define out3(x,y,z) cout << (x) << " " << (y) << " " << (z) << endl
#define out4(x,y,z,w) cout << (x) << " " << (y) << " " << (z) << " " << (w) << endl

const int maxN = 64;

int tot = 50;
int bits[maxN];   //0  1  2  3  4  5  6  7  8
long long bas[9] = {2, 3, 4, 5, 6, 7, 8, 9, 10};
long long val[maxN];
long long fac[maxN];

void dfs(int ind) {
    if( tot == 0 )
        return ;
    if( ind == 0 ) {
        for(int i = 0, j; i < 9; i ++) {
            val[i] = fac[i] = 0;
            for(j = 15; j >= 0; j --)
                val[i] = val[i] * bas[i] + bits[j];
        }
        // 2-10
        for(int i = 0; i < 9; i ++) {
            for(long long p = 2; p * p <= val[i]; p ++) {
                if( val[i] % p == 0 ) {
                    fac[i] = p;
                    break;
                }
            }
            if( fac[i] == 0 ) return ;
        }

        for(int i = 15; i >= 0; i --) printf("%d", bits[i]);
        //for(int i = 0; i < 9; i ++) printf(" %I64d(%I64d)", fac[i], val[i]);
        for(int i = 0; i < 9; i ++) printf(" %I64d", fac[i]);
        printf("\n");

        tot --; return ;
    }
    dfs(ind - 1);
    bits[ind] = 1;
    dfs(ind - 1);
    bits[ind] = 0;
}

void run()
{
    memset(bits, 0, sizeof(bits));
    bits[0] = bits[15] = 1;
    dfs(14);
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    printf("Case #1:\n");
    run();
    return 0;
}
