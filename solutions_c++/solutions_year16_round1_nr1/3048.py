#include <iostream>
#include <fstream>
#include <string>
#include <deque>

using namespace std;

void solve() {
    string s, t="", c;
    cin >> s;
    t.push_back(s[0]);
    for (int i = 1; i < s.size(); ++i) {
        c = s[i];
        if (c + t < t + c)
            t = t + c;
        else
            t = c + t;
    }
    cout << t << "\n";
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, T;
    for (cin >> T, t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
