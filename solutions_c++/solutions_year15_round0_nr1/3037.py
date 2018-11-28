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

int n;
string s;

void solve(int test_number) {
    cin >> n >> s;
    int cur = 0;
    int max_fail = 0;

    for (int i = 0; i <= n; i++) {
        if (cur < i) {
            max_fail += i - cur;  
            cur = i;
        } 
        cur += s[i] - '0';
    }

    cout << "Case #" << test_number << ": " << max_fail << endl;
}

