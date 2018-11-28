#include <bits/stdc++.h>

using namespace std;

void solve() {
    int k;
    cin >> k;
    vector<int> h(2501, 0);
    for (int i = 0; i < k * (2*k-1); ++i) {
        int height;
        cin >> height;
        ++h[height];
    }
    bool first = true;
    for (int i = 0; i < h.size(); ++i) {
        if (h[i] % 2 == 1) {
            if (!first) {
                cout << " ";
            }
            cout << i;
            first = false;;
        }
    }
    cout << endl;
}

int main() {
    int caseNum;
    cin >> caseNum;
    for (int caseIdx = 0; caseIdx < caseNum; ++caseIdx) {
        cout << "Case #" << caseIdx+1 << ": ";
        solve();
    }

    return 0;
}
