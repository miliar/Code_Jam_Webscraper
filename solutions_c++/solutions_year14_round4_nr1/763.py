#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

void solve_slow() {
    int n, x;
    cin >> n >> x;
    int i, j;
    vector <int> A, B;
    A.resize(n);
    B.resize(n, 0);
    for (i = 0; i < n; ++i)
        cin >> A[i];
    sort(A.begin(), A.end());

    int ans = 0;
    for (i = 0; i < n; ++i) {
        if (B[i])
            continue;
        ans++;
        B[i] = 1;
        for (j = n - 1; j >= 0 && !(!B[j] && A[i] + A[j] <= x); --j);
        if (j >= 0)
            B[j] = 1;
    }
    cout << ans << endl;
}

void solve_fast() {
    int n, x;
    cin >> n >> x;
    int i, j;
    set < pair <int, int> > S;
    set < pair <int, int> > :: iterator it;
    for (i = 0; i < n; ++i) {
        cin >> j;
        S.insert(make_pair(-j, i));
    }
    int ans = 0;
    while (!S.empty()) {
        ans++;
        i = S.begin()->first;
        S.erase(S.begin());
        it = S.lower_bound(make_pair(-x - i, -1));
        if (it != S.end())
            S.erase(it);
    }
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, T;
    cin >> T;
    for (t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve_fast();
    }
    return 0;
}