#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T, n, j;
    cin >> T >> n >> j;
    cout << "Case #1:" << endl;

    for (long long i = (1LL << (n - 1)) + 1; i < (1LL << n) && j; i += 2) {
        vector <int> div(11, -1);

        for (int d = 2; d <= 10; d++) {
            long long now = 0;
            long long num = i;
            long long power = 1;

            while (num > 0) {
                now += (num % 2) * power;
                num /= 2;
                power *= d;
            }

            for (int x = 2; x < min(now, 10000LL); x++) {
                if (now % x == 0) {
                    div[d] = x;
                }
            }
        }

        if (*min_element(div.begin() + 2, div.end()) != -1) {
            for (int d = 0; d < n; d++) {
                cout << ((i >> (n - d - 1)) & 1);
            }
            cout << ' ';

            for (int d = 2; d <= 10; d++) {
                cout << div[d] << ' ';
            }
            cout << endl;
            j--;
        }
    }
}
