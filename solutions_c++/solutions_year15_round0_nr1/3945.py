#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int getNumber(char c) {
    return c - '0';
}

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int smax;
        cin >> smax;
        string s;
        cin >> s;
        int cnt = getNumber(s[0]);
        int res = 0;
        for (int i = 1; i <= smax; ++i) {
            int t = getNumber(s[i]);
            if (t == 0) continue;
            if (cnt < i) {
                res += i - cnt;
                cnt = i;
            }
            cnt += t;
        }

        printf("Case #%d: %d\n", test, res);
    }
}
