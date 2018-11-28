#include <bits/stdc++.h>
using namespace std;

string solve(string s) {
    string res = "";
    res.push_back(s[0]);
    for (int i = 1; i < (int)s.size(); ++i) {
        bool f = true;
        for (int j = 0; j < (int)res.size(); ++j)
            if (res[j] > s[i]) {
                f = false;
                break;
            }
        if (f) res.insert(res.begin(), s[i]);
        else res.push_back(s[i]);
    }
    return res;
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests;
    scanf("%d", &nTests);
    for (int t = 1; t <= nTests; ++t) {
        string s;
        cin >> s;

        string res = solve(s);
        printf("Case #%d: ", t);
        cout << res << endl;
    }
}

