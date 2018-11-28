#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define sqr(x) ((x) * (x))
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()

typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef pair <int, int> pii;

void solve(int test) {
    int n;
    cin >> n;
    if (n == 0) {
        cout << "Case #" << test << ": " << "INSOMNIA\n";
        return;
    }
    bool used[10];
    ll res = -1;
    memset(used, false, sizeof(used));
    for (int i = 1; ; i++) {
        ll x = i * 1ll * n;
        while (x > 0) {
            used[x % 10] = true;
            x /= 10;
        }
        bool found = false;
        for (int i = 0; i < 10; i++) {
            if (!used[i]) {
                found = true;
                break;
            }
        }
        if (!found) {
            res = i * 1ll * n;
            break;
        }
    }
    cout << "Case #" << test << ": " << res << "\n";
}

int main() {
    freopen("/Users/nurlan/Dropbox/Programming/contest/contest/input", "r", stdin);
    freopen("/Users/nurlan/Dropbox/Programming/contest/contest/output", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        solve(test);
    }
    return 0;
}