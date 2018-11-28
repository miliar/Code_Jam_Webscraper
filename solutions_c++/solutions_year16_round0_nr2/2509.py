#include <bits/stdc++.h>

int main() {
    int n;
    std::cin >> n;
    for (int tst = 1; tst <= n; ++tst) {
        std::string s;
        std::cin >> s;
        s.push_back('+');
        int res = 0;
        for (std::size_t i = 0; i + 1 < s.size(); ++i) {
            if (s[i] != s[i + 1])
                ++res;
        }
        printf("Case #%d: %d\n", tst, res);
    }
}
