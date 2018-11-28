#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> ans;
int t1, i, j, n, a[20], b[20];
int main() {
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> t1;
        t1--;
        for (j = 0; j < 16; j++){
            cin >> a[j];
            b[j + 1] = 0;
        }

        for (j = 4 * t1; j < 4 * (t1 + 1); j++) {
            b[a[j]] = 1;
        }
        cin >> t1;
        t1--;
        ans.clear();
        for (j = 0; j < 16; j++){
            cin >> a[j];
        }
        for (j = 4 * t1; j < 4 * (t1 + 1); j++) {
            if (b[a[j]] == 1) {
                ans.push_back(a[j]);
            }
        }
        if (ans.size() == 1) {
            cout << "Case #" << i + 1 << ": " << ans[0] << endl;
        }
        else if (ans.size() == 0) {
            cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
        }
        else {
            cout << "Case #" << i + 1 << ": Bad magician!" << endl;
        }

    }

    return 0;
}
