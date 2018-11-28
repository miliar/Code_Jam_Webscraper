#include <bits/stdc++.h>
using namespace std;
template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }
int T;
string s;
ofstream fout("output.txt");

void solve(string s, int cnt) {
    int result = (s[0] == '-');
    char last = s[0];
    for (int i = 1; i < s.length(); ++i) {
        if (last == '+' && s[i] == '-') result += 2;
        last = s[i];
    }
    fout << "Case #" << cnt << ": " << result << endl;
}

int main() {
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> s;
        solve(s, i);
    }
    return 0;
}
