#include <bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define INF 1000000
#define MOD 1000000007
#define ll long long

using namespace std;

ll t, n, ans, c, k;
string s;

int main()
{
    freopen("A.out", "w", stdout);

    cin >> t;
    while (t--) {
        cin >> n;
        cin >> s;
        c = 0, ans = 0;
        for (int i = 0; i <= n; i++)
            if (s[i] != '0') {
                if (c < i) ans += i - c, c = i;
                c += s[i] - 48;
            }
        cout << "Case #" << ++k << ": " << ans << endl;
    }

    return 0;
}
