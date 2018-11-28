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
#include <complex>
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

int t, n, m[1123];

int main(int agrc, char const *argv[])
{
    assert(freopen("A-large.in", "r", stdin));
    assert(freopen("A-large.out", "w", stdout));
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int a1 = 0, a2 = 0, em = 0;
        scanf("%d", &n);
        for (int j = 0; j < n; j++) scanf("%d", &m[j]);
        for (int j = 1; j < n; j++) if (m[j-1] > m[j]) a1 += m[j-1] - m[j];
        for (int j = 1; j < n; j++) em = max(em, m[j-1] - m[j]);
        for (int j = 0; j < n; j++) {
            a2 += min(em, m[j]);
        }
        a2 += max(0, em-m[n-1]);
        printf("Case #%d: %d %d\n", i, a1, a2-em);
    }
    // assert(printf("%fs\n", (double) clock()/CLOCKS_PER_SEC));
    return 0;
}
