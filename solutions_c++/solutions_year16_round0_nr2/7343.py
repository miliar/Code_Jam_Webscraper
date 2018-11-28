#include <bits/stdc++.h>

#define reset(a, b) memset(a, b, sizeof(a))
#define REP(i, a) for (int i = 0; i < a.size(); i++)

using namespace std;

const int N = 100100;
const int INF = 1000000007;

void solve(string s) {
    int ans = 0;
    while (true) {
        int i;
        for (i = 1; i < s.size(); i++)
            if (s[i] != s[i - 1]) break;

        if (i == s.size()){
            if (s[0] == '-')
                ans++;
            break;
        } else {
            for (int j = 0; j < i; j++)
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            ans++;

            bool valid = true;
            REP(j, s) if (s[j] == '-') valid = false;
            if (valid) break;
        }
    }
    cout << ans << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    scanf("%d\n", &T);
    for (int testCase = 1; testCase <= T; testCase++){
        string s;
        getline(cin, s);
        cout << "Case #" << testCase << ": ";
        solve(s);
    }
}
