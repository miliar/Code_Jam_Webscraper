#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> ii;

bool _comp(vector<int> a, vector<int> b) {
    int i = 0;
    while(i < b.size()) {
        if (a[i] < b[i]) {
            return true;
        }
        i++;
    }
    return false;
}

int main(){
    int t, q = 1, n, x;
    int V[3000];
    cin >> t;

    while (t--) {
        cin >> n;
        memset(V, 0, sizeof V);
        for (int i = 0; i < 2*n-1; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> x;
                V[x]++;
            }
        }
        vector<int> ans;
        for (int i = 0; i < 3000; ++i) {
            if (V[i] % 2 == 1) {
                ans.push_back(i);
            }
        }
        sort(ans.begin(), ans.end());
        bool first = true;
        cout << "Case #" << q++ << ": ";
        for (int i = 0; i < ans.size(); ++i) {
            if (first) {
                first = false;
            } else {
                cout << " ";
            }
            cout << ans[i];
        }
        cout << endl;
    }
    return 0;
}
