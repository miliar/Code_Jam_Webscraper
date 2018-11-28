#include<bits/stdc++.h>

using namespace std;

vector<int> arr;

bool solve(int i, int check) {
    vector<int> tmp;

    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] > check) {
            tmp.emplace_back(arr[i] - check);
        }
    }

    for (int j = 0; j < tmp.size(); ) {
        if (tmp[j] > 0 && i == 0) {
            return false;
        }
        if (check >= tmp[j]) {
            j ++;
            i --;
        }
        else {
            tmp[j] -= check;
            i--;
        }
    }

    return true;
}

int main() {
    int t;
    cin >> t;

    int caseno = 0;
    while (t--) {
        arr.clear();

        caseno++;

        int d;
        cin >> d; // diners with non-empty plates

        for (int i = 0; i < d; ++i) {
            int num;
            cin >> num;
            arr.emplace_back(num);
        }

        int mx = *max_element(begin(arr), end(arr));
        int res = 1e9;

        for (int i = 0; i <= mx; ++i) {
            int low = 1, high = mx;
            while (low < high) {
                int mid = (high + low) / 2;
                if (solve(i, mid)) {
                    high = mid;
                }
                else {
                    low = mid + 1;
                }
            }
            res = min(res, i + low);
        }

        cout << "Case #" << caseno << ": " << res << endl;
    }

    return 0;
}