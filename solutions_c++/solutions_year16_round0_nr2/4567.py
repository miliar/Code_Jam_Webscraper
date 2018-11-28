#include <bits/stdc++.h>
using namespace std;

string s;

void flip(int last) {
    for (int i = 0; i <= last; i++)
        s[i] = ((s[i] == '+') ? '-' : '+');
    reverse(s.begin(), s.begin() + last + 1);
}

int solve() {
    const int len = s.length();

    int cnt = 0;
    for (;;) {
        // cout << s << endl;

        if (s[0] == '+') {
            int top = 0;
            while (top < len && s[top] == '+')
                top++;

            if (top >= len) break;

            flip(top - 1);
            cnt++;
        }

        int bot = len - 1;
        while (bot >= 0 && s[bot] == '+')
            bot--;
        // cout << bot << endl;

        if (bot < 0) break;

        flip(bot);
        cnt++;
    }

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int TC; cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        cout << "Case #" << tc << ": ";
        cin >> s;
        cout << solve() << "\n";
    }

    return 0;
}
