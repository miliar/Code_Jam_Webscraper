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
    string S;
    cin >> T;
    for(int t = 0; t < T; t++) {
        string ans = "";
        cin >> S;
        ans += S[0];
        for(int i = 1; i < S.size(); i++) {
            if(ans[0] <= S[i]) {
                ans = S[i] + ans;
            } else {
                ans = ans + S[i];
            }
        }
        cout << "Case #" << t+1 << ": " << ans << endl;
    }
}

