#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int magia(int armin, vector<int> &motes, int n, int i, int moves) {
    if (moves > n) return n;
    if (i == n) return moves;
    if (armin > motes[i]) {
        armin += motes[i];
        return magia(armin, motes, n, i+1, moves);
    }
    else {
        return min(magia(armin, motes, n, i+1, moves+1), magia(2*armin-1, motes, n, i, moves+1));
    }
}

int main () {
    int t;
    int armin, n;
    vector<int> motes;

    cin >> t;

    for (int case_number = 1; case_number <= t; case_number++) {
        cin >> armin >> n;
        motes.clear();
        motes.resize(n);

        for (int i = 0; i < n; i++) cin >> motes[i];
        sort(motes.begin(), motes.end());

        cout << "Case #" << case_number << ": " << magia(armin, motes, n, 0, 0) << endl;
    }

    return 0;
}
