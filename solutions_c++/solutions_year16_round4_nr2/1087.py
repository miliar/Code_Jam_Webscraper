#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int ones(int num) {
    int result = 0;
    while (num > 0) {
        result += num & 1;
        num >>= 1;
    }
    return result;
}

long double tie_prob(vector<long double> probs) {
    long double result = 0;

    for (int subset = 0; subset < (1 << probs.size()); ++subset) {
        if (ones(subset) != probs.size() / 2) continue;

        long double prob = 1;
        for (int i = 0; i < probs.size(); ++i) {
            if (subset & (1 << i)) prob *= probs[i];
            else prob *= 1 - probs[i];
        }
        result += prob;
    }

    return result;
}

int main() {
    int t;
    cin >> t;

    for (int q = 1; q <= t; ++q) {
        int n, k;
        cin >> n >> k;

        long double best = 0;

        vector<long double> probs(n);
        for (int i = 0; i < n; ++i) {
            cin >> probs[i];
        }

        for (int subset = 0; subset < (1 << n); ++subset) {
            if (ones(subset) != k) continue;

            vector<long double> sub_probs;
            for (int i = 0; i < n; ++i) {
                if (subset & (1 << i)) sub_probs.push_back(probs[i]);
            }

            long double tie = tie_prob(sub_probs);

            best = max(best, tie);
        }

        cout << fixed;
        cout << setprecision(10);
        cout << "Case #" << q << ": " << best << endl;
    }
}
