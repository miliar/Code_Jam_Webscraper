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

long long gcd(long a, long b)
{
    if( b == 0 )
        return a;
    return gcd(b, a % b);
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int nt, idx = 0;
    scanf("%d", &nt);
    for(; nt > 0; nt --) {
        long long a, b, ch;
        scanf("%I64d%c%I64d", &a, &ch, &b);
        long long d = gcd(a, b);
        a /= d; b /= d;
        long long n = 0, based = 1;
        while( based < b ) {
            n ++;
            based *= 2LL;
        }
        if( based != b ) {
            printf("Case #%d: impossible\n", ++idx);
            continue;
        }
        long long t = 0; based = 1;
        while( based <= a ) {
            t ++;
            based *= 2LL;
        }
        t --;
        printf("Case #%d: %I64d\n", ++idx, n - t);
    }
    return 0;
}
