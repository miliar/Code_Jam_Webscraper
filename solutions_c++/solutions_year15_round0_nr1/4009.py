#include <vector>
#include <iostream>

int main() {
    int T;
    std::cin >> T;
    // contests make the most horrible code, no validations, etc.
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int Smax;
        std::cin >> Smax;
        std::vector<int> S;
        S.resize(Smax + 1);
        for (int i = 0; i <= Smax; ++i) {
            char c;
            std::cin >> c;
            S[i] = c - '0';
        }
        int friends = 0;
        int standing = 0;
        for (int i = 0; i <= Smax; ++i) {
            if (!S[i]) {
                continue;
            }
            if (i > standing) {
                // next batch won't stand up unless we have enough friends
                int extra = i - standing;
                friends += extra;
                standing += extra;
            }
            standing += S[i];
        }
        std::cout << "Case #" << caseNum << ": " << friends << std::endl;
    }
}
