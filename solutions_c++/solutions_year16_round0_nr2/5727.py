#include <bits/stdc++.h>
#include <string>

using namespace std;

int get_ans(string s) {
    int cnt = 0;
    for (int i = 0; i < s.size() - 1; i++) {
        cnt += (s[i] != s[i + 1]);
    }

    return cnt;
}

inline void print_ans(int s) {
    static int case_num = 0;
    case_num++;
    cout << "Case #" << case_num << ": " << s << "\n";
}

int T;

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);

    ios_base::sync_with_stdio(false);

    cin >> T;

    string s;

    for (int t = 0; t < T; t++) {
        cin >> s;
        s += "+";
        print_ans(get_ans(s));
    }
}
