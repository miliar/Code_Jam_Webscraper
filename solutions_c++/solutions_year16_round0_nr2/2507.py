#include <algorithm>
#include <bitset>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::freopen("in", "r", stdin);
    std::freopen("out", "w", stdout);
    int tn;
    std::cin >> tn;
    for (int ti = 1; ti <= tn; ++ti) {
        std::string s;
        std::cin >> s;
        int n = (int) s.size();
        int answer = 0;
        for (int i = 0; i + 1 < n; ++i) {
            if (s.at(i) != s.at(i + 1)) {
                answer++;
            }
        }
        if (s.back() != '+') {
            answer++;
        }
        std::cout << "Case #" << ti << ": " << answer << std::endl;
    }
}
