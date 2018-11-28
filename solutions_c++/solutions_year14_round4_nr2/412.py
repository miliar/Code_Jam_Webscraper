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
    int N;
    cin >> N;
    vector<pair<int, int> > S(N);
    vector<int> pos(N);
    rep(i, N) {
        int tmp;
        cin >> tmp;
        S[i] = make_pair(tmp, i);
    }
    sort(S.begin(), S.end());
    rep(i, N) {
        pos[S[i].second] = i;
    }
    
    int head = 0, tail = N - 1;
    int ans = 0;
    rep(i, N) {
        int p = S[i].second;
        if (p - head < tail - p) {
            ans += p - head;
            rep(j, p) {
                S[pos[j]].second++;
            }
            for (int j = p; j > 0; j--) {
                swap(pos[j], pos[j-1]);
            }
            head++;
        } else {
            ans += tail - p;
            for (int j = p + 1; j < N; j++) {
                S[pos[j]].second--;
                swap(pos[j-1], pos[j]);
            }
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
