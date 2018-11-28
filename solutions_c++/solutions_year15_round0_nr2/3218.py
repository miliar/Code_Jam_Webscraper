#include <iostream>
#include <string>
using namespace std;

int flattening(int p[], int n, int k) {
    int ans = k;
    for (int i=0; i<n; ++i) {
        if (p[i]<=k) continue;
        int a = p[i]/k;
        ans += a;
        if (a*k==p[i]) --ans;
    }
    return ans;
}

int solve(int p[], int n) {
    int m = p[0];
    for (int i=1; i<n; ++i)
        m = max(m, p[i]);
    int ans = m;
    for (int k=1; k<m; ++k) {
        int cost = flattening(p, n, k);
        ans = min(ans, cost);
    }
    return ans;
}

int main() {
    int T, D; cin >> T;
    for (int i=1; i<=T; ++i) {
        cin >> D;
        int p[D];
        for (int j=0; j<D; ++j) {
            cin >> p[j];
        }
        cout << "Case #" << i << ": " << solve(p, D) << endl;
    }
    return 0;
}
