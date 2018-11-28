#include <iostream>

using namespace std;

void solve(int t) {
    int Smax, i;
    int sum = 0, ans = 0;
    char c;
    cin>>Smax;
    for (i = 0; i <= Smax; i++) {
        cin>>c;
        int n = c - '0';
        if (i == 0) {
            sum = n;
        } else {
            if (sum < i) {
                ans += i - sum;
                sum = i;
            }
            sum += n;
        }
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
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
