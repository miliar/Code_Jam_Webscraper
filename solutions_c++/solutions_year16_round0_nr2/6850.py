#include <bits/stdc++.h>
using namespace std;

map<string,int> m;

int count_ = 0;
int solve(string str) {
    count_++;
    // cout << str << endl;
    if (m.find(str) != m.end()) return m[str];

    m[str] = 1 << 28;
    string head_rev; head_rev += (str[0] == '-' ? '+' : '-');
    int ret = 1 << 28;
    for (int i = 1; i < str.size(); i++) {
        head_rev = (str[i] == '+' ? '-' : '+') + head_rev;

        string next_str = head_rev + string(str.begin() + head_rev.size(), str.end());

        string next_s; next_s += next_str[0];
        for (int j = 1; j < str.size(); j++) {
            if (next_s[next_s.size()-1] == next_str[j]) continue;
            next_s += next_str[j];
        }

        // cout << "# " << head_rev << " " << next_str << " " << next_s << endl;

        ret = min(solve(next_s) + 1, ret);
    }

    // cout << count_ << "% " << str << " " << ret << endl;
    count_--;
    return m[str] = ret;
}

int main() {
    int T;
    cin >> T;

    m["+"] = 0;
    m["-"] = 1;
    m["-+"] = 1;
    m["+-"] = 2;
    m["-+-"] = 3;
    m["+-+"] = 2;
    m["--+"] = 1;
    m["++-"] = 2;
    for (int t = 0; t < T; t++) {
        string str; cin >> str;
        string s; s += str[0];

        for (int i = 1; i < str.size(); i++) {
            if (s[s.size()-1] == str[i]) continue;
            s += str[i];
        }


        // cout << s << endl;
        cout << "Case #" << t + 1 << ": ";
        cout << solve(s) << endl;
    }

    return 0;
}
