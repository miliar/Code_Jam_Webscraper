#include <bits/stdc++.h>
using namespace std;

int get_mask(int i) {
    int ans = 0;
    while (i > 0) {
        ans |= (1 << (i%10));
        i /= 10;
    }
    return ans;
}

void solve(int n) {
    int cur = 0;
    for (int i = 1; i <= 1000; ++i) {
        cur |= get_mask(i*n);
        if (cur == (1 << 10) - 1) {
            cout << i*n << endl;
            return;
        }
    }
    cerr << n << endl;
    cout << "INSOMNIA" << endl;
}

int main() {
    int n, t;
    cin >> t;
    for (int it = 0; it < t; ++it) {
        cin >> n;
        cout << "Case #" << (it+1) << ": ";
        solve(n);
    }
    return 0;
}