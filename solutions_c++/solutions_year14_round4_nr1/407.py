#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <stack>
#include <queue>
#include <set>

#define rep(i,n) for(int i=0;i<(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

void solve() {
    int N, X;
    cin >> N >> X;
    vector<int> S(N);
    rep(i, N) cin >> S[i];
    sort(S.begin(), S.end());
    int ans = 0;
    int hd = 0, tail = N - 1;
    while (hd <= tail) {
        if (hd == tail) {
            ans++;
            break;
        }
        if (S[hd] + S[tail] <= X) {
            ans++;
            hd++;
            tail--;
        } else {
            ans++;
            tail--;
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
