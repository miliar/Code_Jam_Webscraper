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

int test, n, J, finded;
int num[32];
long long res[502][12];
int resnum[502][32];
int F[11][32][4];
const int rem[4] = {2, 3, 5, 7};

bool get(int power, int id) {
    int tmp = 0;
    for (int i = 0; i < n; i++) {
        if (num[i]) {
            tmp = (tmp + F[power][i][id]) % rem[id];
        }
    }
    return (tmp == 0);
}

void check() {
    for (int power = 2; power <= 10; power++) {
        int ok = false;
        for (int i = 0; i < 4; i++) {
            ok = get(power, i);
            if (ok) {
                res[finded][power] = rem[i];
                break;
            }
        }
        if (!ok) {
            return;
        }
    }
    for (int i = 0; i < n; i++) {
        resnum[finded][i] = num[i];
    }
    finded++;
}

void solve(int x) {
    if (finded == J) {
        return;
    }
    if (x == 0) {
        check();
        return;
    }
    num[x] = 1;
    solve(x - 1);
    num[x] = 0;
    solve(x - 1);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    for (int power = 2; power <= 10; power++) {
        for (int t = 0; t < 32; t++) {
            for (int id = 0; id < 4; id++) {
                F[power][t][id] = (!t ? 1 : (F[power][t - 1][id] * power) % rem[id]);
            }
        }
    }
    cin >> test;
    for (int it = 1; it <= test; it++) {
        cin >> n >> J;
        num[0] = 1;
        num[n - 1] = 1;
        finded = 0;
        solve(n - 2);
        cout << "Case #" << it << ":\n";
        for (int i = 0; i < J; i++) {
            for (int j = n - 1; j >= 0; j--) {
                cout << resnum[i][j];
            }
            cout << " ";
            for (int k = 2; k <= 10; k++) {
                cout << res[i][k] << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}
