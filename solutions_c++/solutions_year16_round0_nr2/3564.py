#include <iostream>
#include <array>
#include <vector>
#include <unordered_map>
#include <set>
#include <string>
using namespace std;

int solve(const string& s) {
    int ret = 0;
    for (int i = 1; i < s.length(); ++i) {
        if (s[i] != s[i-1]) ret++;
    }
    if (s.back() == '-') ret++;
    return ret;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        cin >> s;
        auto ans = solve(s);
        cout << "Case #" << (i+1) << ": " << ans << endl;
    }
    return 0;
}
