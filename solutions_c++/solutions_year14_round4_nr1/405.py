#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define X first
#define Y second

const int MAX_N = 100001;
const int MAX_M = 100001;
const int MOD = 1e9 + 7.5;
const double EPS = 1e-8;

int n, m;
int a[MAX_N];

void init() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> a[i];
}

void solve(int ca) {
    sort(a, a + n);
    int i = 0, j = n - 1, cnt = 0;
    while (i <= j) {
        ++cnt;
        if (i < j) {
            if (a[i] + a[j] <= m) {
                ++i, --j;
            } else {
                --j;
            }
        } else {
            ++i;
        }
    }
    printf("Case #%d: %d\n", ca, cnt);
}

int main(){
    freopen("b1.in", "r", stdin);
	freopen("b1.out", "w", stdout);
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        init();
        solve(i + 1);
    }
    return 0;
}
