#include <cstdio>
#include <string>
#include <algorithm>
#include <utility>
using namespace std;

constexpr char imp[] = "IMPOSSIBLE";

string solve(int n, int r, int p, int s) {
    if(r < 0 || p < 0 || s < 0)
        return imp;
    if(n == 0) {
        if(r) return "R";
        if(p) return "P";
        if(s) return "S";
        return imp;
    }
    string next = solve(n - 1, (s + r - p) / 2,
            (p + r - s) / 2, (p + s - r) / 2);
    if(next == imp)
        return imp;
    string ans = "";
    for(char c : next)
        switch(c) {
            case 'R': ans += "RS"; break;
            case 'P': ans += "PR"; break;
            case 'S': ans += "PS"; break;
        }
    return ans;
}

string mini(const string &s) {
    if(s == imp) return imp;
    if(s.size() == 1) return s;
    string s1 = mini(s.substr(0, s.size() / 2));
    string s2 = mini(s.substr(s.size() / 2, s.size()));
    return s1 < s2 ? s1 + s2 : s2 + s1;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        printf("Case #%d: %s\n", i, mini(solve(n, r, p, s)).c_str());
    }
}

