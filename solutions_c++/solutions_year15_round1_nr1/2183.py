#include<bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for(int i=a;i<b;i++)
const int MX = 1e6 + 6;
int ar[MX];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, n;
    cin >> t;
    int a, b, maxi;
    FOR(T, 0, t) {
        a = 0;b = 0;
        cin >> n;
        FOR(i, 0, n) cin >> ar[i];
        maxi = 0;
        FOR(i, 1, n) maxi = max(maxi, ar[i-1] - ar[i]);
        FOR(i, 1, n) {
            if(ar[i-1] > ar[i]) a += ar[i-1] - ar[i];
        }
        FOR(i, 0, n-1) {
            b += min(ar[i], maxi);
        }
        printf("Case #%d: %d %d\n",T+1, a, b);
    }
    return 0;
}
