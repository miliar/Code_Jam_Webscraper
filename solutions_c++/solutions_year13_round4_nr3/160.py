#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <deque>
#include <string>
#include <string.h>
#include <queue>
#include <stdlib.h>
#include <set>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

const int N = 2222;
int n;
int a[N], b[N], x[N], u[N];
vector<int> ans;
vector<int> best;
int l[N], r[N];

void rec(int X) {
    if (X == n) {
        if (best.size() == 0 || ans < best) {
            best = ans;
        }
        return;
    }

    vector<int> sons;
    for (int i = 0; i < n; ++i) {
        if (ans[i] != -1) {
            l[i] = a[i];
        } else {
            l[i] = 0;
        }
        if (i) l[i] = max(l[i], l[i - 1]);
    }
    for (int i = n - 1; i >= 0; --i) {
        if (ans[i] != -1) {
            r[i] = b[i];
        } else {
            r[i] = 0;
        }
        r[i] = max(r[i], r[i + 1]);
    }
    for (int pos = 0; pos < n; ++pos) 
        if (ans[pos] == -1 && l[pos] + 1 == a[pos] && r[pos] + 1 == b[pos]) {
            sons.push_back(pos);
        }

    for (int i = 0; i < sons.size(); ++i) {
        ans[sons[i]] = X;
        rec(X + 1);
        ans[sons[i]] = -1;
    }
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int _T;
    scanf("%d\n", &_T);

    for (int __test = 1; __test <= _T; ++__test) {
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        memset(l, 0, sizeof(l));
        memset(r, 0, sizeof(r));
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        for (int i = 0; i < n; ++i) {
            cin >> b[i];
        }

        while (!ans.empty()) ans.pop_back();
        while (!best.empty()) best.pop_back();
        for (int i = 0; i < n; ++i) ans.push_back(-1);

        rec(0);

        printf("Case #%d: ", __test);
        for (int i = 0; i < n; ++i) cout << best[i] + 1 << " ";
        cout << endl;
    }


    return 0;
}

