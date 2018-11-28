#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair <int, int> ii;
typedef vector <int> vi;
typedef double ld;
#define X first
#define Y second
#define mk make_pair
#define pb push_back
#define Rep(i, n) for(int i = 0; i < int(n); i ++)
const int MOD = (int) 1e9 + 7;
void MAIN();
int main(){
    //freopen("input.txt", "r", stdin);
    ios:: sync_with_stdio(false); cin.tie(0);
    MAIN();
    return 0;
}
////////////////////////////////////////////////////////////////////////

const int N = 32;
double f[N][N], p[N];

void MAIN(){
    int tc;
    cin >> tc;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) f[i][j] = 0;
    }
    cout.precision(8);
    for (int cs = 1; cs <= tc; ++cs) {
        int n, k;
        cin >> n >> k;
        for (int i = 1; i <= n; ++i) cin >> p[i];
        double ans = 0;
        for (int sub = 1; sub < 1 << n; ++sub) {
            if (__builtin_popcount(sub) != k) continue;
            vector <int> id;
            for (int i = 0; i < n; ++i) if (sub & 1 << i) id.push_back(i+1);
            f[0][0] = 1;
            for (int i = 1; i <= k; ++i) {
                for (int j = 0; j <= i; ++j) {
                    f[i][j] = f[i-1][j] * (1-p[id[i-1]]);
                    if (j > 0) f[i][j] += f[i-1][j-1] * p[id[i-1]];
                }
            }
            ans = max(ans, f[k][k/2]);
        }
        cout << fixed << "Case #" << cs << ": " << ans << endl;
        cerr << fixed << "Case #" << cs << ": " << ans << endl;
    }
}
