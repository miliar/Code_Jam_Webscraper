#include <bits/stdc++.h>

typedef long long ll;
#define pb push_back
#define mp make_pair
#define in freopen("A-large.in", "r", stdin)
#define out freopen("out", "w", stdout)
#define home in; out
#define fi first
#define se second
#define SZ(V) (int) V.size()
#define LN(V) (int) V.length()
#define ALL(V) V.begin(), V.end()
using namespace std;

int t, k;
string s;

int main() {

    ios_base::sync_with_stdio(0);

    home;

    cin >> t;

    for (int j = 1; j <= t; j++) {

        cin >> k >> s;

        int sum = 0, res = 0;

        for (int i = 0; i < SZ(s); i++) {

            if (s[i] != '0') {

                if (i > sum)
                    res += i - sum, sum = i;
            }

            sum += s[i] - '0';
        }

        cout << "Case #" << j << ": " << res << "\n";
    }

    return 0;
}
