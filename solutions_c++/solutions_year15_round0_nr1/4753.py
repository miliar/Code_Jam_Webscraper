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
#define elif else if
#define mp make_pair
#define pb push_back
#define len(a) (a).size()
#define cosl __builtin_cosl
#define sinl __builtin_sinl
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

int t;

int main(int agrc, char const *argv[])
{
    assert(freopen("A-large.in", "r", stdin));
    assert(freopen("A-large.out", "w", stdout));
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i+1);
        int m, mem[1123], l, ans = 0;
        char s[1123];
        scanf("%d %s", &m, s);
        l = strlen(s);
        mem[0] = s[0] - '0';
        for (int j = 1; j < l; j++) mem[j] = mem[j-1] + s[j] - '0';
        for (int j = l-1; j >= 0; j--) {
            if (mem[j-1] + ans < j) ans = j - mem[j-1];
        }
        printf("%d\n", ans);
    }
    // assert(printf("%fs\n", (double) clock()/CLOCKS_PER_SEC));
    return 0;
}
