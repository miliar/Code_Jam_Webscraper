#include <iostream>

using namespace std;

void solve(int t) {
    int n, i, m[1010];
    int sum = 0;
    cin>>n;
    for ( i = 0; i < n; i++ ) {
        cin>>m[i];
        sum += m[i];
    }
    int ans1 = 0, max = 0;
    for ( i = 0; i < n-1; i++ ) {
        int now = m[i] - m[i+1];
        if (now > 0) {
            ans1 += now;
            if (now > max) {
                max = now;
            }
        }
    }
    int ans2 = 0;
    for ( i = 0; i < n-1; i++ ) {
        if (m[i] < max) {
            ans2 += m[i];
        } else {
            ans2 += max;
        }
    }
    cout<<"Case #"<<t<<": "<<ans1<<" "<<ans2<<endl;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t, i;
    cin>>t;
    for (i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
