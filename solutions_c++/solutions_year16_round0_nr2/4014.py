# include <iostream>
# include <cmath>
# include <algorithm>
# include <map>
# include <unordered_set>
# include <memory.h>
# include <vector>
using namespace std;
 
 
const int MD = 1000000000 + 7;
const int MAX_E = 500333;
const int MAX_N = 1047;

#define time ez_contest
#define rank ez_timus

bool used[10];

void doTheShit(string& s) {
    for (int i = 0; i + 1 < s.size(); i++) {
        if (s[i] != s[i + 1]) {
            for (int j = 0; j <= i; j++) {
                s[j] = s[i + 1];
            }
            return;
        }
    }
}

void solve(int tc) {
    cout << "Case #" << tc << ": ";
    string s;
    cin >> s;
    int ans = 0;
    while (true) {
        bool minus = false, plus = false;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '+') {
                plus = true;
            } else {
                minus = true;
            }
        }
        if (minus && plus) {
            ans++;
            doTheShit(s);
            continue;
        }
        if (minus) {
            ans++;
        }
        cout << ans << "\n";
        return;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve(t);
    }
    return 0;
}

