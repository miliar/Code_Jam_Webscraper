/* template by isprime */
#ifndef tty
#define NDEBUG
#endif

#include <bits/stdc++.h>

using namespace std;

#define st first
#define gcd __gcd
#define nd second
#define mp make_pair
#define pb push_back
#define typeof __typeof
#define cosl __builtin_cosl
#define len(a) ((a).size())
#define sinl __builtin_sinl
#define fabsl __builtin_fabsl
#define sqrtl __builtin_sqrtl
#define atan2l __builtin_atan2l
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)>(b)?(b):(a))
#define bitcount __builtin_popcount
#define all(a) (a).begin(),(a).end()

typedef string str;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vii;

int t, n, mem[1123456];

inline int rev(int x)
{
    str y = to_string(x);
    reverse(all(y));
    return stoi(y);
}

int main(int agrc, char const *argv[])
{
    assert(freopen("A-small-attempt3.in", "r", stdin));
    assert(freopen("A-small-attempt3.out", "w", stdout));
    for (int i = 1; i <= 1000000; i++) {
        mem[i] = mem[i-1] + 1;
        int r = rev(i), rr = rev(r);
        if (r < i && rr == i) mem[i] = min(mem[i], mem[r] + 1);
    }
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d", &n);
        printf("Case #%d: %d\n", i, mem[n]);
    }
    // assert(printf("%fs\n", (double) clock()/CLOCKS_PER_SEC));
    return 0;
}
