#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)

using namespace std;

void solve() {
    set<int> used;
    int n;
    cin >> n;
    rep (i, 1000) {
        int tmp = n * (i + 1);
        while (tmp > 0) {
            used.insert(tmp % 10);
            tmp /= 10;
        }
        if (used.size() == 10) {
            n = n * (i + 1);
            break;
        }
        if (i == 999) {
            cout << "INSOMNIA" << endl;
            return;
        }
    }
    cout << n << endl;
}

int main() {
    int N;
    cin >> N;
    rep(i, N) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
