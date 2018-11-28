/* template by isprime */
#ifndef tty
    #define NDEBUG
#endif

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <iterator>
#include <algorithm>

using namespace std;

#define st first
#define gcd __gcd
#define nd second
#define it iterator
#define mp make_pair
#define pb push_back
#define len(a) (a).size()
#define cosl __builtin_cosl
#define sinl __builtin_sinl
#define rit reverse_iterator
#define fabsl __builtin_fabsl
#define sqrtl __builtin_sqrtl
#define atan2l __builtin_atan2l
#define bitcount __builtin_popcount
#define all(a) (a).begin(),(a).end()

typedef string str;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vii;

int t, l, x, p;
char s[11234];
ll lx;

inline int pow2(int x)
{
    int b = 2, r = 1;
    while (x) {
        if (x % 2) r *= b;
        b *= b;
        x /= 2;
    }
    return r;
}

inline int calc(int a, int b)
{
    if (a < 0) return -calc(-a, b);
    else if (a == 1) return b;
    else if (a == 2) {
        if (b == 2) return -1;
        else if (b == 4) return 8;
        else return -4;
    } else if (a == 4) {
        if (b == 2) return -8;
        else if (b == 4) return -1;
        else return 2;
    } else {
        if (b == 2) return 4;
        else if (b == 4) return -2;
        else return -1;
    }
}

int main(int agrc, char const *argv[])
{
    assert(freopen("C-small-attempt0.in", "r", stdin));
    assert(freopen("C-small-attempt0.out", "w", stdout));
    scanf("%d", &t);
    for (int n = 1; n <= t; n++) {
        printf("Case #%d: ", n);
        scanf("%d %d", &l, &x);
        scanf("%s", s);
        lx = l*x;
        bool fi = 0, fj = 0, fk = 0;
        int v = 1;
        for (p = 0; p < lx && !fi; p++) {
            v = calc(v, pow2(s[p%l] - 'h'));
            fi = v == 2;
        }
        if (p == lx) {
            printf("NO\n");
            continue;
        } else v = 1;
        for (; p < lx && !fj; p++) {
            v = calc(v, pow2(s[p%l] - 'h'));
            fj = v == 4;
        }
        if (p == lx) {
            printf("NO\n");
            continue;
        } else v = 1;
        for (; p < lx; p++) v = calc(v, pow2(s[p%l] - 'h'));
        fk = v == 8;
        if (fi && fj && fk) printf("YES\n");
        else printf("NO\n");
    }
    // assert(printf("%fs\n", (double) clock()/CLOCKS_PER_SEC));
    return 0;
}
