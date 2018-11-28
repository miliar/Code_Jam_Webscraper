#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

string solve() {
    vector<int> candidates[2];
    for (int ind = 0; ind < 2; ++ind) {
        size_t row;
        cin >> row; --row;
        vector< vector<int> > nums(4, vector<int>(4));
        for (size_t i = 0; i < 4; ++i)
            for (size_t j = 0; j < 4; ++j)
                cin >> nums[i][j];
        candidates[ind] = nums[row];
    }

    int ans = -1;
    for (size_t i = 0; i < 4; ++i) {
        const int num = candidates[0][i];
        vector<int>::const_iterator it = find(candidates[1].begin(), candidates[1].end(), num);
        if (it == candidates[1].end())
            continue;
        if (ans != -1)
            return "Bad magician!";
        ans = *it;
    }
    if (ans == -1)
        return "Volunteer cheated!";
    ostringstream oss;
    oss << ans;
    return oss.str();
}

int main() {
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        const string& result = solve();
        cout << "Case #" << t << ": " << result << '\n';
    }

    return 0;
}

