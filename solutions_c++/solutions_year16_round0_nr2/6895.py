#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool ShouldContinue(const string& s) {
    for (size_t i = 0; i < s.size(); ++i)
        if (s[i] == '-')
            return true;
    return false;
}

void Solve() {
    string s;
    cin >> s;
    int steps = 0;
    while (ShouldContinue(s)) {
        size_t i = 0;
        if (s[i] == '-') {
            while (i < s.size() && s[i] == '-')
                ++i;
            ++steps;
            s = string(i, '+') + s.substr(i);
        } else {
            while (i < s.size() && s[i] == '+')
                ++i;
            int st = i;
            int len = 1;
            while (st + len < s.size() && s[st + len] == '-')
                ++len;
            s = string(st + len, '+') + s.substr(st + len);
            steps += 2;
        }
    }
    cout << steps << endl;
}

int main() {
    int t;
    string s;
    getline(cin, s);
    t = atoi(s.c_str());
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        Solve();
    }
    return 0;
}
