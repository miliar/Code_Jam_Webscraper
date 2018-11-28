#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

bool achive_goal(int m, int c, vector<int> &a) {
    for (int i = 0; i < a.size(); i++) {
        c -= (a[i] - 1) / m;
        if (c < 0) {
            return false;
        }
    }
    return true;
}

int main() {
    ifstream cin("input");
    ofstream cout("output");

    int t;
    cin >> t;

    for (int l = 0; l < t; l++) {
        int d;
        cin >> d;
        
        vector<int> a(d);

        for (int i = 0; i < d; i++) {
            cin >> a[i];
        }
        sort(a.begin(), a.end());
        reverse(a.begin(), a.end());
        int max_spits = a[0];
        int max_num = a[0];
        int ans = a[0];

        for (int cur_splits = 0; cur_splits <= max_spits; cur_splits++) {
            int l = 0, r = max_num, m;
            while(r - l > 1) {
                m = (r + l) / 2;
                if (achive_goal(m, cur_splits, a)) {
                    r = m;
                } else {
                    l = m;
                }
            }
            ans = min(ans, cur_splits + r);
        }

        cout << "Case #" << l + 1 << ": " << ans << endl;
    }
}
