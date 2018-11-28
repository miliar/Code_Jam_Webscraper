#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

#define rep(i,n) for (int i = 0; i < int(n); i++)

template <class T> void setmax(T& x, T const& y) { x = max(x, y); }
template <class T> void setmin(T& x, T const& y) { x = min(x, y); }

int main() {
    int T; cin >> T;
    rep (t,T) {
        cout << "Case #" << t+1 << ": ";
        const int MAX = 10010;
        int N, X, S[MAX];
        rep (i,MAX) S[i] = 0;
        cin >> N >> X;
        rep (i,N) cin >> S[i];

        sort(S, S+N);

        int ans = 0;

        int j = N-1;
        rep (i,N) {
            while (true) {
                if (i > j) break;
                if (i < j && S[i] + S[j] > X) {
                    ans++;
                    j--;
                    continue;
                }
                if (i == j) {
                    ans++;
                    goto answer;
                }
                ans++;
                j--;
                break;
            }
        }
    answer:
        cout << ans << endl;
    }
}
