#include <cstdio>
#include <string>
#include <iostream>
#include <bitset>

using namespace std;

#define PROBLEM "A-large"

string solve(string s) {
    string r = s.substr(0, 1);
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] < r[0])
            r = r + s[i];
        else
            r = s[i] + r;
    }
    return r;
}

int main()
{
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        cin >> s;
        cout << "Case #" << t << ": " << solve(s) << endl;
    }

    return 0;
}
