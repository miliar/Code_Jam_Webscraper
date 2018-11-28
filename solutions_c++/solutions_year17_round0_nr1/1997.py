#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)



string S; int K;
int sol() {
    int N = S.length();
    int ans = 0;
    rep(i, 0, N - K + 1) if (S[i] == '-') {
        rep(j, 0, K) {
            if (S[i + j] == '-') S[i + j] = '+';
            else S[i + j] = '-';
        }
        ans++;
    }
    rep(i, 0, N) if (S[i] == '-') return -1;
    return ans;
}
//-----------------------------------------------------------------------------------
int main() {
    int T; cin >> T;
    rep(t, 1, T + 1) {
        cin >> S >> K;
        int ans = sol();
        if(ans < 0) printf("Case #%d: IMPOSSIBLE\n", t);
        else printf("Case #%d: %d\n", t, ans);
    }
}