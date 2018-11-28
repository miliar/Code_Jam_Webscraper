#include <iostream>
#include <string>
using namespace std;

int T, n;
string s;

inline intv(char c) {
    return c - '0';
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    for (int I = 1; I <= T; I++) {
        cin >> n >> s;
        int sum = 0, ans = 0;
        for (int i = 0; i < s.size(); i++) {
            if (sum < i) {
                ans += i - sum;
                sum = i;
            }
            sum += intv(s[i]);
        }
        printf("Case #%d: %d\n", I, ans);
    }
    return 0;
}
