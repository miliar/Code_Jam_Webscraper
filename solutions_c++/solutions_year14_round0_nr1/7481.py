#include <bits/stdc++.h>
#define msg(x) cout << #x << " = " << x << endl
using namespace std;

int t, idx;
std::vector<int>::iterator it;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> idx;
        vector<int> v1, v2;
        for (int i = 1; i <= 4; i++) {
            int x;
            for (int j = 0; j < 4; j++) {
                cin >> x;
                if (i == idx) v1.push_back(x);
            }
        }
        cin >> idx;
        for (int i = 1; i <= 4; i++) {
            int x;
            for (int j = 0; j < 4; j++) {
                cin >> x;
                if (i == idx) v2.push_back(x);
            }
        }
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        vector<int> v(10);
        it = std::set_intersection (v1.begin(), v1.end(), v2.begin(), v2.end(), v.begin());
        v.resize(it-v.begin());
        cout << "Case #" << tc << ": ";
        if (v.size() == 0) {
            cout << "Volunteer cheated!";
        } else if (v.size() > 1) {
            cout << "Bad magician!";
        } else {
            cout << v[0];
        }
        cout << "\n";
    }
    return 0;
}
