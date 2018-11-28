#include <bits/stdc++.h>

using namespace std;

#define mem(a, v) memset(a, v, sizeof (a))
#define x first
#define y second
#define all(a) (a).begin(), (a).end()
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
#define rep(i, n) for (int i = 0; i < int(n); i ++)
#define repi(i, a, n) for (int i = (a); i < int(n); i ++)
#define repe(x, v) for (auto x: (v))

int modu(int n) {
    int ret = 0;
    while (n > 0) {
        ret |= (1 << (n%10));
        n /= 10;
    }
    return ret;
}

int main () {
    std::ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    repi(t, 1, T+1) {
        cout << "Case #" << t << ": ";
        int n;
        cin >> n;
        if (n == 0) {
            cout << "INSOMNIA\n";
        } else {
            int b = 0, p = 0;
            while (b != 1023) {
                p += n;
                b |= modu(p);
            }
            cout << p << "\n";
        }
    }
    return 0;
}
