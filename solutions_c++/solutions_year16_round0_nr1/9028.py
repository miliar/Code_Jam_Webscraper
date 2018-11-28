#include <bits/stdc++.h>
using namespace std;

int n, t;
bool used[10];

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);

    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";

        cin >> n;

        for (int i = 0; i < 10; i++) used[i] = false;

        long long m = 0;
        int cnt = 0, j;
        for (j = 1; j <= 1000000 && cnt < 10; j++) {
            m = (long long) n * j;
            while (m) {
                cnt += !used[m % 10];
                used[m % 10] = true;
                m /= 10;
            }
        }
        if (cnt != 10) cout << "INSOMNIA\n";
        else cout << (long long)(j - 1) * n << "\n";
    }



    return 0;
}
