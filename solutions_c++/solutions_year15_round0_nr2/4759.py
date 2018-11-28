#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <ctime>
#include <string>

using namespace std;

#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll rdtsc() {
    ll tmp;
    asm("rdtsc" : "=A"(tmp));
    return tmp;
}

inline int myrand() {
    return abs((rand() << 15) ^ rand());
}

inline int rnd(int x) {
    return myrand() % x;
}

#define TASKNAME "text"
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
#define INF ((int)1e9)
#define sqr(x) ((x) * (x))
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())


const int maxn = 2000;
int p[maxn];

void solve() {
    int d;
    scanf("%d",&d);
    for (int i = 0; i < d; i++) {
        scanf("%d",&p[i]);
    }

    int best = maxn;
    for (int r = 1; r <= maxn; r++) {
        int cur = r;
        for (int i = 0; i < d; i++) {
            cur += (p[i] + r - 1) / r - 1;
        }
        best = min(best, cur);
    }
    printf("%d\n", best);
}

int main() {
    srand(rdtsc());
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        printf("Case #%d: ", t + 1);
        solve();
        eprintf("%.18lf\n", (double)clock() / CLOCKS_PER_SEC);
    }
    return 0;
}

