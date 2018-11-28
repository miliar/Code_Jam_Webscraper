#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define pp pair<int, int>
#define fi first
#define se second
#define esp 1e-9
#define inf 1000000001
#define mod 1000000007
#define N 2222
#define M 15
typedef long long ll;
typedef long double ld;
using namespace std;
int nt, n, x;
int d[2555];

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> nt;
    for (int  kk = 1; kk <= nt; kk++) {
        memset(d, 0, sizeof(d));
        cin >> n;
        for (int i = 1; i < 2 * n; i++) {
            for (int j = 1; j <= n; j++) {
                cin >> x;
                d[x]++;
            }
        }

        cout << "Case #" << kk << ": ";
        for (int i = 1; i <= 2500; i++)
            if (d[i] % 2 != 0) cout << i << " ";
        cout << "\n";
    }
    /**/return 0;
}
