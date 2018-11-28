#include <bits/stdc++.h>
using namespace std;
const int N = 110;
queue <string> qq;
map <string, int> mp;
string nxt(string s, int p) {
    int l = s.length();
    for (int i = 0, j = p; i <= j; i++, j--) {
        if ( i == j) {
            if (s[i] == '+') s[i] = '-';
            else s[i] = '+';
            continue;
        }
        swap(s[i], s[j]);
        if (s[i] == '+') s[i] = '-';
        else s[i] = '+';
        if (s[j] == '+') s[j] = '-';
        else s[j] = '+';
    }
    return s;
}
int solve (string s) {
    string ee;
    int n = s.length();
    for (int i = 0; i < n; ++i) ee.push_back('+');
    if (s == ee) return 0;
    mp.clear();
    mp[s] = 0;
    while (!qq.empty()) qq.pop();
    qq.push(s);
    while (!qq.empty()) {
        string u = qq.front(); qq.pop();
        int cost = mp[u];
        for (int i = 0; i < n; ++i){
            string v = nxt(u, i);
            if (mp.find(v) == mp.end()) {
                mp[v] = cost + 1;
                if (v == ee) return cost + 1;
                qq.push(v);
            }
        }
    }
}
int main() {
    //freopen("B.in", "r", stdin);
    //freopen("B.out", "w", stdout);
     int ntest; cin >> ntest;

    for (int test = 1; test <= ntest; ++test) {
        string s;
        cin >> s;
        cout << "Case #" << test << ": " << solve(s) << endl;
    }
    return 0;
}

