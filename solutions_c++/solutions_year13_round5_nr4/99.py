#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

typedef long long LL;
const LL MOD = 1000002013;

map<string, double> memo;

double f(string& s) {
    if (memo.count(s)) return memo[s];
    double res = 0;

    for (int i = 0; i < s.length(); ++i) {
        int j = i;
        int c = s.length();
        while (s[j] == 'X' && c > 0) {
            --c; j = (j + 1) % s.length();
        }
        if (!c) return 0;
        s[j] = 'X';
        res += c + f(s);
        s[j] = '.';
    }

    return memo[s] = res / s.length();
}

void solve() {
    
    string s;
    cin >> s;

    static int testid;
    cout << fixed;
    cout.precision(10);
    cout << "Case #" << ++testid << ": " << f(s) << endl;
}

int main() {
    int tests;
    cin >> tests;
    while (tests --> 0)
        solve();
    return 0;
}
