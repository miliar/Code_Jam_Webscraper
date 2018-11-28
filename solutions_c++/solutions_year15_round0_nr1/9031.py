#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int t, m;
string s;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int k = 1; k <= t; ++k) {
        cin >> m;
        cin >> s;
        int cnt = 0, ans = 0;
        for (int i = 0; i <= m; ++i)
            if (cnt >= i)
                cnt += (s[i] - '0');
            else
                ans += (i - cnt), cnt += (i - cnt), cnt += (s[i] - '0');
        cout << "Case #" << k << ": " << ans << endl;
    }
    return 0;
}
