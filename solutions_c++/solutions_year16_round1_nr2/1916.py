#include <bits/stdc++.h>

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> Pair;
typedef complex<double> Complex;

const double PI = M_PI;
const int INF = 1e9;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int n, a;
        cin >> n;
        vector<int> memo(2501, 0);
        for(int i = 0; i < 2*n - 1; i++) {
            for(int j = 0; j < n; j++) {
                cin >> a;
                memo[a]++;
            }
        }

        vector<int> ans;

        for(int i = 1; i <= 2500; i++) {
            if(memo[i] & 1) ans.emplace_back(i);
        }

        sort(ans.begin(), ans.end());

        cout << "Case #" << t << ":";
        for(int i = 0; i < ans.size(); i++) cout << " " << ans[i];
        cout << endl;
    }
}

