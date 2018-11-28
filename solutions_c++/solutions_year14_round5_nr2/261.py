#include <iostream>
#include <vector>
#include <map>

using namespace std;

int p, q;
vector<int> gs;

struct Compare {
    bool operator()(const vector<int> &a, const vector<int> &b) const {
        return lexicographical_compare(a.begin(), a.end(), b.begin(), b.end());
    }
};

map<vector<int>, int, Compare> memo;

int backtrack(vector<int> &hps) {

    if (memo.count(hps))
        return memo[hps];

    int best = 0;
    bool go = false;

    for (auto i : hps) {
        if (i > 0)
            go = true;
    }

    if (!go)
        return 0;

    for (int i = 0; i <= hps.size(); i++) {
        int gold = 0;

        if (i < hps.size() && hps[i] > 0) {
            hps[i] -= p;
            if (hps[i] <= 0)
                gold += gs[i];
        } else if (i < hps.size()) {
            continue;
        }

        int j = 0;

        for (j = 0; j < hps.size(); j++) {
            if (hps[j] > 0) {
                hps[j] -= q;
                break;
            }
        }

        if (j < hps.size()) {
            gold += backtrack(hps);
        }

        best = max(best, gold);

        if (i < hps.size())
            hps[i] += p;

        if (j < hps.size())
            hps[j] += q;
    }

    memo[hps] = best;

    return best;
}

int main() {

    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n;
        cin >> p >> q >> n;
        gs.resize(n);
        vector<int> hps(n);

        for (int i = 0; i < n; i++)
            cin >> hps[i] >> gs[i];

        memo.clear();

        cout << "Case #" << tc << ": " << backtrack(hps) << '\n';
    }

    return 0;
}

