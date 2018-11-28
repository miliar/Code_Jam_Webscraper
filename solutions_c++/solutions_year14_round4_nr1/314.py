#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 1e5 + 5;
int Tc, n, m;
int a[N];

int main() {
    scanf("%d", &Tc);
    rep (ri, Tc) {
        printf("Case #%d: ", ri + 1);
        scanf("%d%d", &n, &m);
        rep (i, n) scanf("%d", &a[i]);
        sort(a, a + n);
        int j = n - 1;
        int ans = 0;
        rep (i, n) {
            while (i < j && a[i] + a[j] > m) {
                j--;
            }
            if (i < j) {
                ans++;
                j--;
            }
        }
        printf("%d\n", n - ans);
    }
}

