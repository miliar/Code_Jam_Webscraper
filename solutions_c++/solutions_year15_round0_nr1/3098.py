#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())

using namespace std;
typedef long long LL;
typedef pair <int, int> pii;

int t;

int main() {    
    //freopen(".in", "r", stdin);
    //freopen(".out", "w", stdout);

    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        string s;
        cin >> n >> s;
        int bal = 0;
        int ans = 0;
        for (int j = 0; j <= n; ++j) {
            if (s[j] != '0' && bal < j) {
                ans += j - bal;
                bal = j;
            }
            bal += s[j] - '0';
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }

    return 0;
}