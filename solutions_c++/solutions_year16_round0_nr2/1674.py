#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const int max_n = 111, inf = 1111111111;

int t;
vector<char> v;
string s;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        cin >> s;
        for (int i = 0; i < s.length(); ++i) {
            v.push_back(s[i]);
        }
        int ans = 0;
        char c = '+';
        while (v.size()) {
            if (v.back() == c) {
                v.pop_back();
                continue;
            }
            if (c == '+') {
                c = '-';
            } else {
                c = '+';
            }
            v.pop_back();
            ++ans;
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
