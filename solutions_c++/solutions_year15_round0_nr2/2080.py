#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        int D;
        std::cin >> D;
        std::vector<int> P(D);
        for (int d = 0;d < D; ++d) {
            std::cin >> P[d];
        }
        std::sort(P.begin(), P.end(), std::greater<int>());

        int best = P[0];
        int eats = P[0];
        for (int e = eats; e > 0; --e) {
            int splits = 0;
            for (int d = 0; d < D; ++d) {
                if (P[d] <= e) {
                    break;
                }
                splits += (P[d] - 1) / e;
            }
            if (e + splits < best) {
                best = e + splits;
            }
            if (splits >= best)
                break;
        }

        std::cout << "Case #" << t << ": " << best << std::endl;
    }
}

