#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <sstream>
using namespace std;

int tests, n;
string s;

int main() {
    cin >> tests;
    for (int cases = 1; cases <= tests; ++ cases) {
        cin >> s;
        n = s.length();
        vector <char> t;
        t.clear();
        t.push_back(s[0]);
        for (int i = 1; i < n; ++ i) {
            if (s[i] == t.back()) t.pop_back();
            else t.push_back(s[i]);
        }
        int ans = 5 * n - (t.size() / 2) * 5;
        cout << "Case #" << cases << ": " << ans << endl;
    }
    return 0;
}

