#include <iostream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <limits>
#include <cassert>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <string>


void run_test_case()
{
    std::string S;
    long K;
    std::cin >> S >> K;

    /* std::cerr << "\nS = " << S << "   K = " << K << '\n'; */

    int flips = 0;
    for (unsigned int i = 0; i <= S.size() - K; ++i) {
        if (S[i] != '+') {
            assert(S[i] == '-');
            flips += 1;
            for (unsigned int j = 0; j < K; ++j) {
                char& c = S[i+j];
                c = (c != '+') ? '+' : '-';
                // could use this check to advance i to the nearest '-'
            }
        }
    }
    /* std::cerr << "\nS = " << S << "   K = " << K << '\n'; */

    // actually need only check the last K-1 slots but whatever
    for (unsigned int i = 0; i < S.size(); ++i) {
        if (S[i] != '+') {
            std::cout << "IMPOSSIBLE";
            return;
        }
    }
    std::cout << flips;
}


int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
