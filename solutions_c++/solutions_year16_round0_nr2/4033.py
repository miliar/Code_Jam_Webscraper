# include <iostream>
# include <cmath>
# include <algorithm>
# include <map>
# include <vector>
using namespace std;
 
  bool used[10];



void solve(int test) {
    string s;
    cout << "Case #" << test << ": ";
    cin >> s;
    int n = s.length();
    int res = 0;
    for(;;) {
        bool f1 = false, f2 = false;
        for (int i = 0; i < s.size(); i++) {
            f1 = f1 || (s[i] == '-');
            f2 = f2 || (s[i] == '+');
        }
        if (f1 && f2) {
            for (int i = 0; i + 1 < n; i++) {
                if (s[i] != s[i + 1]) {
                    for (int j = 0; j <= i; j++) {
                        s[j] = s[i + 1];
                    }
                    break;
                }
            }
            res++;
            continue;
        }
        cout << res+int(f1==true) << endl;
        return;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        solve(t);
    }
    return 0;
}

