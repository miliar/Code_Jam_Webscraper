#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for(int test = 0; test < tests; test++) {
        string s;
        int mx;
        cin >> mx >> s;
        int up = 0;
        int ans = 0;
        int pos = 0;
        while (pos < (int)s.size()) {
            if (up >= pos) {
                up += (s[pos] - '0');
                pos++;
            } else {
                ans += (pos - up);
                up = pos;
            }
        }
        printf("Case #%d: %d\n", test+1, ans);
    }
	return 0;
}
