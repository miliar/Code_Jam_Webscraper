#include <iostream>

using namespace std;

void solve(int t) {
    int D, P[1010];
    int i, now, j;
    int max = 0, ans = (~0) ^ (1 << 31);
    cin>>D;
    for (i = 0; i < D; i++) {
        cin>>P[i];
        if (P[i] > max) {
            max = P[i];
        }
    }
    for (i = 1; i <= max; i++) {
        now = i;
        for (j = 0; j < D; j++) {
            now += ( (P[j] + i - 1) / i ) - 1;
        }
        // cout<<now<<endl;
        if (now < ans) {
            ans = now;
        }
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int t, i;
    cin>>t;
    for (i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
