#include <iostream>
#include <cassert>


int solve(int R, int C, int W) {
    if (W == C) {
        return R + W - 1;
    }

    if (W == 1) {
        return R * C;
    }

    int score = 0;

    // pin it down, at least one of these must be a hit
    score = R * (C / W);

    assert(W < C);
    score += W;

    if (C % W == 0) {
        score -= 1; // touches wall
    }

    return score;
}


void run_test_case()
{
    int R, C, W;
    std::cin >> R >> C >> W;

    std::cout << solve(R, C, W);
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
