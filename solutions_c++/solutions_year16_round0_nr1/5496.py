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

long long foo(long long x) {
    long long s = 0;
    do {
        s |= 1LL << (x % 10);
        x /= 10;
    } while( x );
    return s;
}

long long run(long long n)
{
    long long val = n, status = 0;
    for(long long beg = 1; beg < 10086; beg ++) {
        status |= foo(val * beg);
        if( status == (1LL << 10) - 1 )
            return val * beg;
    }
    return -1;
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int nt, idx = 0;
    scanf("%d", &nt);
    for(long long n; nt > 0; nt --) {
        scanf("%I64d", &n);
        n = run(n);
        if( n == -1LL )
            printf("Case #%d: INSOMNIA\n", ++ idx);
        else
            printf("Case #%d: %I64d\n", ++ idx, n);
    }
    return 0;
}
