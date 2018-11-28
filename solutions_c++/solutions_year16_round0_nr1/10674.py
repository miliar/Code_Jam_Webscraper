#include <bits/stdc++.h>

using namespace std;

#ifndef int64
#define int64 long long
#endif

template <typename T> void pv(vector<T> v) {
    for (auto i : v) {
        cout << i << " ";
    }
    cout << endl;
}

bool is(vector<bool> &u) {
    for (bool i : u) {
        if (!i)
            return 0;
    }
    return 1;
}

bool isInsomnia(int64 n) { return n == n * 2 && n == n * 3 && n == n * 4; }

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    cin >> T;

    int64 n;
    for (int i = 1; i <= T; i++) {
        cin >> n;
        if (isInsomnia(n)) {
            cout << "Case #" << i << ": INSOMNIA\n";
            continue;
        }
        vector<bool> u(10, 0);
        for (int64 j = 1;; j++) {
            int64 k = n * j;
            while (k) {
                u[k % 10] = 1;
                k /= 10;
            }
            if (is(u)) {
                cout << "Case #" << i << ": " << (n * j) << endl;
                break;
            }
            k *= j;
        }
        // pv(u);
    }
    return 0;
}