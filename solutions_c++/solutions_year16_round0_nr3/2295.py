#include <bits/stdc++.h>

using namespace std;

int cnt = 0;

long long get_div(long long x) {
    for (int i = 2; i <= 100; i++) {
        if (x % i == 0)
            return i;
    }
    return 1;
}

void solve() {
    int N = 15;
    int J = 50;
    vector < long long > ans;
    for (int mask = (1 << (N)) + 1; mask < (1 << (N + 1)); mask += 2) {
        vector < int > repr;
        repr.clear();
        int x = mask;
        for (int i = 0; i <= N; i++) {
            repr.push_back(x % 2);
            x /= 2;
        }
        bool ok = true;
        for (int base = 2; base <= 10; base++) {
            long long num = 0;
            long long st = 1;
            for (auto xj : repr) {
                num += st * xj;
                st = st * base;
            }
            if (get_div(num) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) {
            for (int i = repr.size() - 1; i >= 0; i--)
                cout << repr[i];
            cout << " ";
            for (int base = 2; base <= 10; base++) {
                long long num = 0;
                long long st = 1;
                for (auto xj : repr) {
                    num += st * xj;
                    st = st * base;
                }
                cout << get_div(num) << " ";
            }
            cnt++;
            if (cnt == J) {
                return;
            } else {
                cout << endl;
            }
        }

    }
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test = 1;
    for (int id = 1; id <= test; id++){
        cout << "Case #" << id << ":\n";
        solve();
    }
    return 0;
}