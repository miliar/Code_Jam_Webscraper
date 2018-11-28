#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int war(set< double > as, set< double > bs) {
    int score = 0;
    while (!as.empty()) {
        auto a = as.begin();
        auto b = bs.upper_bound(*a);
        if (b == bs.end()) {
            score += 1;
            b = bs.begin();
        }
        as.erase(a);
        bs.erase(b);
    }
    return score;
}

int dwar(set< double > as, set< double > bs) {
    int score = 0;
    while (!as.empty()) {
        auto a = as.begin();
        auto b = bs.begin();
        if (*a > *b) {
            score += 1;
        }
        else {
            b = bs.end();
            --b;
        }
        as.erase(a);
        bs.erase(b);
    }
    return score;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n;
        cin >> n;
        set< double > as;
        set< double > bs;
        for (int i = 0; i < n; ++i) {
            double x;
            cin >> x;
            as.insert(x);
        }
        for (int i = 0; i < n; ++i) {
            double x;
            cin >> x;
            bs.insert(x);
        }
        cout << "Case #" << t << ": "
             << dwar(as, bs) << " "
             << war(as, bs) << "\n";
    }
    return 0;
}
