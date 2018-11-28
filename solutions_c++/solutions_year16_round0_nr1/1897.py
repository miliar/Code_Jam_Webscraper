#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

int ans[1001000];

int get_mask(int x) {
    if (x == 0) return 1;
    int mask = 0;
    while (x) {
        int d = x % 10;
        x /= 10;
        mask |= (1 << d);
    }
    return mask;
}

int res = 0;

int solve(int x) {
    int mask = 0;
    for (int iter = 1; iter <= 72; iter++) {
        mask |= get_mask(iter * x);
        res = max(res, iter * x);
        if (mask == (1 << 10) - 1) return iter * x;
    }
    return -1;
}

int main(){

    for (int i = 0; i <= (int)1e6; i++) {
        ans[i] = solve(i);
    }

    int t;
    int x;

    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        scanf("%d", &x);
        if (ans[x] == -1) printf("INSOMNIA\n");
        else printf("%d\n", ans[x]);
    }

    return 0;
}
