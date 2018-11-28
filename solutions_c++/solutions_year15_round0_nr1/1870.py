#include <iostream>
#include <string>
#include <vector>

using namespace std;

string KillSpace(const string& s) {
    string res;
    for (size_t i = 0; i < s.size(); ++i)
        if (s[i] != ' ')
            res.push_back(s[i]);
    return res;
}

void Solve() {
    int sMax;
    cin >> sMax;
    string s;
    getline(cin, s, '\n');
    s = KillSpace(s);

    int standing = s[0] - '0';
    int res = 0;
    for (size_t i = 1; i < s.size(); ++i) {
        if (s[i] == '0')
            continue;
        if (standing < i) {
            int add = i - standing;
            res += add;
            standing += add;
        }
        standing += s[i] - '0';
    }
    cout << res << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        Solve();
    }
    return 0;
}
