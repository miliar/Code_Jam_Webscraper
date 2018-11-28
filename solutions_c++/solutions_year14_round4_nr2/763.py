#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define For(i,a,b) for(int i=a;i<=b;i++)
#define For2(i,a,b) for(int i=a;i<b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
#define OUT(x) {cout << #x << " = " << x << endl;}
#define FOUT(x,a,b) {cout << #x << " = "; For(_,a,b) cout << x[_] << ' '; cout << endl;}
#define FOUT2(x,a,b,c,d) {cout << #x << " = " << endl; For(_,a,b){For(__,c,d) cout << x[_][__] << " "; cout << endl;}}
#define fi first
#define se second
#define mp make_pair
#define sz(x) (int)x.size()
#define BIT(s,i) ((s&(1<<i))>0)

typedef long long ll;

int n, a[1111], f[1111][1111], pos[1111];
pair<int, int> b[1111];
int preL[1111], preR[1111];
int mark[1111];

void solve() {
    scanf("%d", &n);
    For(i, 1, n) {
        scanf("%d", &a[i]);
        b[i] = mp(a[i], i);
    }
    sort(b + 1, b + 1 + n);
    For(i, 1, n) {
        a[b[i].se] = i;
        pos[i] = b[i].se;
    }

    For(i, 1, n) {
        mark[i] = 0;
        preR[i] = 0;
        preL[i] = 0;
    }
    For(i, 1, n) {
        For(j, pos[i] + 1, n) if (!mark[j]) ++preR[i];
        Ford(j, pos[i] - 1, 1) if (!mark[j]) ++preL[i];
        mark[pos[i]] = 1;
    }

    For(i, 1, n) {
        f[0][i] = f[0][i - 1] + preR[i];
        f[i][0] = f[i - 1][0] + preL[i];
    }

    For(i, 1, n)
        For(j, 1, n - i) {
            int k = i + j;
            f[i][j] = min(f[i - 1][j] + preL[k], f[i][j - 1] + preR[k]);
        }
    int res = 1000000000;
    For(i, 1, n)
        res = min(res, f[i][n - i]);
    printf("%d\n", res);
}

int main() {

#ifndef ONLINE_JUDGE
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif

    int T;
    scanf("%d", &T);
    For(i, 1, T) {
        printf("Case #%d: ", i);
        solve();
    }

}
