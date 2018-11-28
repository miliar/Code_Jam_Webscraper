#include <bits/stdtr1c++.h>

#define MAX 205
#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define dbg(x) cout << #x << " = " << x << endl
#define write() freopen("out.txt", "w", stdout)

using namespace std;

int n, m, k;
bool visited[MAX][415];
double ar[MAX], lol[MAX], dp[MAX][415];

double F(int i, int d){
    if (i == m) return (d == 0);
    if (visited[i][d + MAX]) return dp[i][d + MAX];
    double res = (lol[i] * F(i + 1, d + 1)) + ((1.0 - lol[i]) * F(i + 1, d - 1));
    visited[i][d + MAX] = true;
    return (dp[i][d + MAX] = res);
}

int main(){
    read();
    write();
    double x, res;
    int T = 0, t, i, j, l;

    scanf("%d", &t);
    while (t--){
        scanf("%d %d", &n, &k);
        for (i = 0; i < n; i++) scanf("%lf", &ar[i]);
        sort(ar, ar + n);

        res = 0.0;
        for (i = 0; i <= k; i++){
            for (m = 0, j = 0, l = n - 1; j < i; j++) lol[m++] = ar[j];
            while (m < k) lol[m++] = ar[l--];

            clr(visited);
            x = F(0, 0) + 1e-12;
            if (x > res) res = x;
        }
        printf("Case #%d: %0.9f\n", ++T, res);
    }
    return 0;
}
