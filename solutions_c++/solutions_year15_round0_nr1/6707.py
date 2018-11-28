#include <bits/stdc++.h>

using namespace std;

typedef long long  ll;

int Solve(int s_max, string s)
{
    s = string(s_max + 1 - s.size(), '0') + s;

    const int n = s.size();
    int res = 0, sum = 0;

    for (int i = 0; i < n; ++i) {
        int num = (int)(s[i] - '0');

        if (i > sum) {
            res += i - sum;
            sum += i - sum;
        }
        sum += num;
    }

    return res;
}

int main()
{
    ios::sync_with_stdio(false);

    int T, s_max;
    string s;

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> s_max >> s;
        cout << "Case #" << t << ": " << Solve(s_max, s) << "\n";
    }

    return 0;
}
