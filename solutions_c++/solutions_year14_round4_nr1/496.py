#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

void solve() {
    int N, X;
    cin >> N >> X;
    vector<int> a(N);
    for (int i = 0; i < N; i++)
        cin >> a[i];
    sort(a.begin(), a.end());
    vector<int> :: iterator st = a.begin(), ed = a.end();
    int ans = 0;
    for (; st < ed; ans++) {
        ed--;
        if (st != ed && *st + *ed <= X)
            st++;
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        solve();
    }
}