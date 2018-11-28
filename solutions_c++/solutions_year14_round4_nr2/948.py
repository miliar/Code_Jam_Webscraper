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

        const int MAX = 1111;
        int N, A[MAX], B[MAX];
        rep (i,MAX) A[i] = B[i] = 0;

        cin >> N;
        rep (i,N) cin >> A[i], B[i] = A[i];
        sort(B, B+N); reverse(B, B+N);

        int ans = 0;
        rep (i,N) {
            int L = 0, R = 0;
            int j = 0;
            for ( ; A[j] != B[i]; j++) if (A[j] > B[i]) L++;
            for (j++ ; j < N ; j++) if (A[j] > B[i]) R++;
            ans += min(L, R);
        }

        cout << ans << endl;
    }
}
