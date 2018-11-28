#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <memory.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>

#define NAME "test-large"

#define EPS (1e-9)
#define INF ((int)(1e+9))
#define LINF ((long long)(1e+18))

#define ve vector<int>
#define pb push_back

#define pii pair<int, int>
#define mp make_pair
#define fi first
#define se second
#define fs first
#define sc second

using namespace std;

typedef long long li;
typedef long long ll;
typedef long long lint;

void solve(int test_number);

int main() {
#ifdef _GEANY
    freopen(NAME ".in", "r", stdin);
    freopen(NAME ".out", "w", stdout);
#else
#endif
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
    int n = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i + 1);
    }
    return 0;
}

const int MAXN = 1010;

int n, new_n;
int a[MAXN];
int new_a[MAXN * MAXN];

int check(int cnt) {
    int res = 0;
    for (int i = 0; i < n; i++) {
        int turns = a[i] / cnt;
        if (a[i] % cnt != 0)
            turns++;
        turns--;
        res += turns;
    }
    return res;
}

void solve(int test_number) {
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int res = INF;
    for (int i = 1; i <= MAXN; i++) {
        res = min(res, i + check(i));
    }
    cout << "Case #" << test_number << ": " << res << endl;
}

