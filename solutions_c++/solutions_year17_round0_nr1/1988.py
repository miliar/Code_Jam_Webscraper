#include <iostream>
#include <queue>

using namespace std;

//map<pair<int, pair<int, bool>>, int64_t>
string solve(string& s, int k) {
    int count = 0;
    size_t n = s.size();
    for (size_t i = 0; i + k <= n; ++i) {
        if (s[i] == '-') {
            ++count;
            for (size_t j = 0; j < k; ++j) {
                char &c = s[i + j];
                if (c == '-')
                    c = '+';
                else
                    c = '-';
            }
        }
    }

    for (auto i : s) {
        if (i == '-')
            return "IMPOSSIBLE";
    }
    return to_string(count);
}

int main() {
    int T = 10000;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << t << ": " << solve(s, k) << endl;
    }
}