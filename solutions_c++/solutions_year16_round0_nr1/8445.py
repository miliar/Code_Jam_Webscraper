#include <bits/stdc++.h>

using namespace std;

int T, N;

int mark[10];

void markDigit(int x) {
    while (x) {
        mark[x % 10] = 1;
        x /= 10;
    }
}

bool check() {
    for (int i = 0; i < 10; ++i)
        if (!mark[i])
            return false;
    return true;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        if (N == 0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
            continue;
        }
        memset(mark, 0, sizeof mark);
        int x = N;
        markDigit(x);
        while (!check()) {
            x += N;
            markDigit(x);
        }
        cout << "Case #" << t << ": " << x << endl;
    }
}
