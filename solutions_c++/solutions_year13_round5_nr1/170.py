#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

double f(const vector<int>& bets, int hole, int height, int budget) {
    // ensure that there are hole columns that has height height
    // and the rest has height > height
    int budget_needed = 0;
    if (bets[hole-1] > height) {
        // already not possible
        return 0.0;
    }
    for (int i = 0; i < hole; i++) {
        budget_needed += height - bets[i];
    }
    for (int i = hole; i < bets.size(); i++) {
        if (bets[i] < height + 1) {
            budget_needed += height + 1 - bets[i];
        }
    }
    if (budget_needed > budget) {
        // money not enough
        return 0.0;
    }
    double expected_winnings = 0.0;
    for (int i = 0; i < hole; i++) {
        expected_winnings += 36.0 * (height - bets[i]) / hole;
    }
    return expected_winnings - budget_needed;
}

int main() {

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        double ans = 0.0;

        int budget;
        int bet_count;
        cin >> budget >> bet_count;
        vector<int> bets(37);
        for (int i = 0; i < bet_count; i++) {
            cin >> bets[i];
        }
        sort(bets.begin(), bets.end());

        for (int hole = 1; hole <= 37; hole++) {
            for (int height = 1; height <= 2000; height++) {
                double winning = f(bets, hole, height, budget);
                ans = max(ans, winning);
            }
        }

        printf("Case #%d: %.9lf\n", t, ans);
    }

    return 0;
}

