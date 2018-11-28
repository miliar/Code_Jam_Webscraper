#include <bits/stdc++.h>
using namespace std;
long long n;
bool valid[11];
bool check(long long u) {
    while(u) {
        valid[u%10] = true;
        u /= 10;
    }
    for (int i = 0; i < 10; ++i) if (valid[i] == false) return 0;
    return 1;
}
int main() {
    //freopen("A.inp", "r", stdin);
    //freopen("A.out", "w", stdout);
    ios::sync_with_stdio(false); cin.tie();

    int ntest; cin >> ntest;

    for (int test = 1; test <= ntest; ++test) {
        cin >> n;
        memset(valid, false, sizeof valid);
        long long ans = -1;
        for (int i = 1; n != 0 && i < INT_MAX; ++i) {
            long long u = n * i;
            if (check(u)) { ans = u; break; }
        }
        if (ans != -1) cout << "Case #" << test << ": " << ans << endl;
        else cout << "Case #" << test << ": " << "INSOMNIA" << endl;
    }
    return 0;
}

