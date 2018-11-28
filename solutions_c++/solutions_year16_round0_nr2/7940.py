#include <iostream>
using namespace std;

int main () {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t;
    cin >> t;
    string s;
    for (int i = 1 ; i <= t; i++) {
        cin >> s;
        int ans = 0;
        int p = 0;
        while (p < s.size() && s[p] == '-') p++;
        if (p != 0) ans += 1;
        string news = "+";
        char prev = '+';
        for (int j = p; j < s.size(); j++) {
            if (prev != s[j]) {
                news += s[j];
                prev = s[j];
            }
        }
        for (int j = 0; j < news.size(); j+=2) {
            if (j+1 < news.size() && news[j] == '+' && news[j+1] == '-') {
                ans += 2;
            }
        }
        cout << "Case #" << i<< ": ";
        cout << ans << endl;
    }
    return 0;
}