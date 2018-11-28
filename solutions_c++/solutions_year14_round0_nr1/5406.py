#include <iostream>
#include <vector>

using namespace std;

vector<int> getCounts() {
    int R; 
    cin >> R;
    R--;
    vector<int> v(16, 0);
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            int cur;
            cin >> cur;
            cur--;
            if (R == i) v[cur]++;
        }
    }
    return v;
}

void solve() {
    vector<int> c1 = getCounts();
    vector<int> c2 = getCounts();
    int ans = -1;
    int seen = 0;
    for (int i = 0; i < 16; ++i) {
        if (c1[i] > 0 && c2[i] > 0) {
            seen++;
            ans = i;
        }
    }
    if (seen == 0) {
        cout << "Volunteer cheated!" << endl;
    } else if (seen > 1) {
        cout << "Bad magician!" << endl;
    } else {
        cout << ans+1 << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}