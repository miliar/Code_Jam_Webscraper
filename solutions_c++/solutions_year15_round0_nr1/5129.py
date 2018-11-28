#include<bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for(int i=a;i<b;i++)
const int MX = 1e6 + 6;
char s[MX];
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, n;
    int till, ans, req, here;
    cin >> t;
    FOR(T, 0, t) {
        cin >> n >> s;
        till = 0;
        ans = 0;
        FOR(i, 0, n+1) {
            req = i;
            if(req > till) here = req - till;
            else here = 0;
            ans += here;
            till += s[i] - '0';
            till += here;
        }
        printf("Case #%d: %d\n",T+1, ans);
    }
    return 0;
}
