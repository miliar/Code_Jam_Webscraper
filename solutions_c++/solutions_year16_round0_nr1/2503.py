#pragma comment (linker, "/STACK:128000000")
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>
#include <string>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int MAXN = 2e5 + 200;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test, n;
bool visited[10];

bool solve(long long x) {
    while (x) {
        visited[x % 10] = true;
        x /= 10;
    }
    bool ok = true;
    for (int i = 0; i < 10; i++) {
        if (!visited[i]) {
            ok = false;
            break;
        }
    }
    return ok;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    scanf("%d", &test);
    for (int it = 1; it <= test; it++) {
        scanf("%d", &n);
        long long ans = -1;
        for (int delta = 1; delta <= 1000; delta++) {
            if (solve(1LL * n * delta)) {
                ans = 1LL * n * delta;
                break;
            }
        }
        for (int i = 0; i < 10; i++) {
            visited[i] = false;
        }
        if (ans == -1) {
            printf("Case #%d: INSOMNIA\n", it);
        } else {
            printf("Case #%d: %d\n", it, ans);
        }
    }
    return 0;
}
