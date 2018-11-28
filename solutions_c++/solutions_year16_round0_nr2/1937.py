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

int T;
int ans[11][1 << 11];
int n;
int d[1 << 11];
int used[1 << 11];

int reverse(int mask, int k) {
    int ans = 0;
    for (int i = 0; i < k; i++) {
        if ((1 << i)&mask) {
            ans |= (1 << (k - 1 - i));
        }
    }
    return ans;
}

int invert(int mask, int k) {
    return mask^((1 << k) - 1);
}

int rotate(int mask, int k) {
    int d = (1 << (n - k)) - 1;
    d *= (1 << k);
    int ans = mask&d;
    int last = mask&((1 << k) - 1);
    last = reverse(last, k);
    last = invert(last, k);
    return last|ans;
}

void solve() {
    for (int i = 0; i < (1 << n); i++) d[i] = inf, used[i] = 0;
    d[0] = 0;
    queue <int> q;
    q.push(0);
    used[0] = 1;
    while (!q.empty()) {
        int mask = q.front(); q.pop();
        for (int i = 1; i <= n; i++) {
            int nmask = rotate(mask, i);
            if (!used[nmask]) {
                d[nmask] = d[mask] + 1;
                used[nmask] = 1;
                q.push(nmask);
            }
        }
    }
    for (int i = 0; i < (1 << n); i++) ans[n][i] = d[i];
}

int calc(string s) {
    int n = sz(s);
    int mask = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '-') mask |= (1 << i);
    }
    return ans[n][mask];
}

int main(){

    for (n = 1; n <= 10; n++) {
        solve();
    }

    cin >> T;

    for (int i = 1; i <= T; i++) {
        string s;
        cin >> s;
        printf("Case #%d: %d\n", i, calc(s));
    }

    return 0;
}
