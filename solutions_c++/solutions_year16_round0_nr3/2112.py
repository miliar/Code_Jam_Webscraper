#include <bits/stdc++.h>

using namespace std;

int check(vector<int> &digits) {
    vector<int> ans;
    for (int i = 2; i <= 10; ++i) {
        __int128 p = 1;
        __int128 kol = 0;
        for (int j = 0; j < (int)digits.size(); ++j) {
            kol = kol + p * digits[j];
            p *= i;
        }
        bool flag = false;

        for (int j = 2; j <= 10000; ++j) {
            if (kol % j == 0) {
                flag = true;
                ans.push_back(j);
                break;
            }
        }
        if (!flag)
            return 0;
    }
    reverse(digits.begin(), digits.end());
    for (int i = 0; i < (int)digits.size(); ++i)
        cout << digits[i];
    cout << ' ';
    for (int i = 0; i < (int)ans.size(); ++i)
       cout << ans[i] << ' ';
    cout << '\n';
    reverse(digits.begin(), digits.end());
    return 1;
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n, kol;
        cin >> n >> kol;
        cout << "Case #" << i + 1 << ":" << '\n';
        long long p = 1;
        for (int i = 0; i < n - 1; ++i)
            p *= 2;

        for (long long i = p; i < p * 2 && kol > 0; ++i) {
            if (i % 2 == 0)
                continue;
            vector<int> digits;
            long long j = i;
            while (j > 0) {
                digits.push_back(j % 2);
                j /= 2;
            }
            kol -= check(digits);
        }

    }
    return 0;
}
