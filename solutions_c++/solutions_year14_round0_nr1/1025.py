#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

set< int > read_row() {
    set< int > res;
    int row;
    cin >> row;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 1; j <= 4; ++j) {
            int x;
            cin >> x;
            if (i == row) {
                res.insert(x);
            }
        }
    }
    return res;
}

vector< int > solve() {
    auto a = read_row();
    auto b = read_row();
    vector< int > res;
    set_intersection(a.begin(), a.end(), b.begin(), b.end(), back_inserter(res));
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        auto ans = solve();
        if (ans.empty()) {
            cout << "Volunteer cheated!";
        }
        else if (ans.size() > 1) {
            cout << "Bad magician!";
        }
        else {
            cout << ans.front();
        }
        cout << "\n";
    }
    return 0;
}
