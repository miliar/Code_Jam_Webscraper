#include <bits/stdc++.h>
using namespace std;


void solve(int test) {
    int ans1;
    cin >> ans1;
    --ans1;
    int a[4][4];
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> a[i][j];
        }
    }
    set<int> nums;
    for (int i = 0; i < 4; ++i) {
        nums.insert(a[ans1][i]);
    }
    int ans2;
    cin >> ans2;
    --ans2;

    int b[4][4];
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> b[i][j];
        }
    }
    set<int> ans;
    for (int i = 0; i < 4; ++i) {
        if (nums.count(b[ans2][i])) {
            ans.insert(b[ans2][i]);
        }
    }

    cout << "Case #" << test << ": ";
    if (ans.size() == 1) {
        cout << *ans.begin() << endl;
    } else {
        if (ans.empty()) {
            cout << "Volunteer cheated!" << endl;
        } else {
            cout << "Bad magician!" << endl;
        }
    }
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
    return 0;
}
