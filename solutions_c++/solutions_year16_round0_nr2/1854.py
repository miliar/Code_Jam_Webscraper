#include <bits/stdc++.h>

using namespace std;

int solve() {
    string s;
    cin >> s;
    int reg = 1;
    for(int i = 1; i < s.length(); i++)
        if (s[i] != s[i - 1]) reg++;
    int res = reg - (s[s.length() - 1] == '+');
    return res;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int ntests;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; tc++) {
        cout << "Case #" << tc << ": " << solve() << endl;
    }
}
