#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        string str;
        cin >> str;
        str += "+";

        int ans = 0;
        for (int i = 0; i + 1 < str.length(); i++) {
            if (str[i] != str[i+1])
                ans++;
        }

        cout << "Case #" << tc << ": " << ans << "\n";
    }
}

