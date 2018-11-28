#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <limits>
#include <algorithm>
#include <ctime>
#include <unordered_map>
#include <unordered_set>
#include <cstring>

using namespace std;

int cs = 0, n, ans;
int c[10];
vector<string> f[100];

string solve(int n, char ch) {
    if (n == 1) return string("") + ch;
    string ans = "";
    if (ch == 'R') {
        string a = solve(n - 1, 'R');
        string b = solve(n - 1, 'S');
        ans = a < b ? a + b : b + a;
    } else if (ch == 'S') {
        string a = solve(n - 1, 'P');
        string b = solve(n - 1, 'S');
        ans = a < b ? a + b : b + a;
    } else {
        string a = solve(n - 1, 'P');
        string b = solve(n - 1, 'R');
        ans = a < b ? a + b : b + a;
    }
    return ans;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    for (int i = 1; i < 15; ++i) {
        f[i - 1].push_back(solve(i, 'R'));
        f[i - 1].push_back(solve(i, 'S'));
        f[i - 1].push_back(solve(i, 'P'));
    }
    int t;
    cin>>t;
    while (t--) {
        cin>>n;
        for (int i = 0; i < 3; ++i) cin>>c[i];
        printf("Case #%d: ",++cs);
        vector<string> ans;
        for (int i = 0; i < 3; ++i) {
            int rcnt = 0, pcnt = 0, scnt = 0;
            for (auto ch : f[n][i]) {
                if (ch == 'R') ++rcnt;
                else if (ch == 'P') ++pcnt;
                else ++scnt;
            }

            if (rcnt == c[0] && pcnt == c[1] && scnt == c[2]) {
                ans.push_back(f[n][i]);
            }
            sort(ans.begin(), ans.end());
        }
        if (ans.empty()) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans[0]<<endl;

    }
    return 0;
}
