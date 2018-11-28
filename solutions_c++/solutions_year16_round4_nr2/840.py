#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

double doit(int bit, int N, int K, vector<double>& P) {
    vector<double> prob(N + 2);
    prob[0] = 1;
    rep(i, N) {
        if ((bit >> i) & 1) {
            vector<double> newprob(N + 2);
            rep(j, N + 1) {
                newprob[j] += prob[j] * (1 - P[i]);
                newprob[j + 1] += prob[j] * P[i];
            }
            prob = newprob;
        }
    }
    //cerr << bit << ": " << prob[K / 2] << endl;
    return prob[K / 2];
}

void solve() {
    int N, K;
    cin >> N >> K;
    vector<double> P(N);
    rep(i, N) {
        cin >> P[i];
    }
    sort(P.begin(), P.end());
    
    double ans = 0;
    rep(i, 1 << N) {
        if (__builtin_popcount(i) != K) continue;
        
        ans = max(ans, doit(i, N, K, P));
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
