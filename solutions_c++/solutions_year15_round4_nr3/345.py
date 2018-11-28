#include <bits/stdc++.h>

using namespace std;

#define lol long long
#define fi first
#define se second
#define pb push_back
#define sz(s) (lol)s.size()
#define must ios_base::sync_with_stdio(0)

#define inp(s) freopen(s, "r", stdin)
#define out(s) freopen(s, "w", stdout)

vector <string> v[210];
set<string> s[3];
int us[210][2010];
int ans;

void rec(int cur) {
//    cout << cur << "\n";
//    cout << "\t" << s[0].size() << ' ' << ans << "\n";
    if(s[0].size() >= ans)
        return;
    if(cur == 2) {
        ans = min(ans, (int)s[0].size());
        return;
    }
    int i;
    string x;
    for(i = 0; i < v[cur].size(); i++) {
        x = v[cur][i];
        us[cur][i] = 0;
        if(s[0].find(x) == s[0].end() && s[2].find(x) != s[2].end()) {
            us[cur][i] += 1;
            s[0].insert(x);
        }
        if(s[1].find(x) == s[1].end()) {
            us[cur][i] += 2;
            s[1].insert(x);
        }
    }
    rec(cur - 1);
    for(i = 0; i < v[cur].size(); i++) {
        x = v[cur][i];
        if(us[cur][i] > 1) {
            us[cur][i] -= 2;
            s[1].erase(s[1].find(x));
        }
        if(us[cur][i] == 1) {
            us[cur][i]--;
            s[0].erase(s[0].find(x));
        }
    }
    for(i = 0; i < v[cur].size(); i++) {
        x = v[cur][i];
        us[cur][i] = 0;
        if(s[0].find(x) == s[0].end() && s[1].find(x) != s[1].end()) {
            us[cur][i] += 1;
            s[0].insert(x);
        }
        if(s[2].find(x) == s[2].end()) {
            us[cur][i] += 2;
            s[2].insert(x);
        }
    }
    rec(cur - 1);
    for(i = 0; i < v[cur].size(); i++) {
        x = v[cur][i];
        if(us[cur][i] > 1) {
            us[cur][i] -= 2;
            s[2].erase(s[2].find(x));
        }
        if(us[cur][i] == 1) {
            us[cur][i]--;
            s[0].erase(s[0].find(x));
        }
    }







}

int main() {
    inp("input.txt");
    out("output.txt");
    int tt, t;
    cin >> t;
    for(tt = 1; tt <= t; tt++) {
        int n, i;
        char c;
        string d = "";
        scanf("%d\n", &n);
        for(i = 1; i <= n; i++)
            v[i].clear();
        for(i = 1; i <= n; i += (c == '\n')) {
            scanf("%c", &c);
            if(c == ' ' || c == '\n') {
                v[i].pb(d);
                d = "";
            } else {
                d += c;
            }
        }
//        cout << n << "\n";
//        for(i = 1; i <= n; i++, cout << "\n")
//            for(auto x: v[i])
//                cout << x << ' ';
        s[1].clear();
        s[2].clear();
        s[0].clear();
        ans = 1000000000;
        for(auto x: v[1])
            s[1].insert(x);
        for(auto x: v[2]) {
            if(s[1].find(x) != s[1].end()) {
                s[0].insert(x);
                s[1].erase(s[1].find(x));
            }
            else
                s[2].insert(x);
        }
        rec(n);
        cout << "Case #" << tt << ": " << ans << "\n";
    }
}

