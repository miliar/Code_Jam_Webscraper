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

int T, X, N;
int s[11111];
int mark[11111], res;

void solve() {
    scanf("%d%d", &N, &X);
    For(i, 1, N) scanf("%d", &s[i]);
//    FOUT(s, 1, N);
    sort(s + 1, s + 1 + N);
    res = 0;
    For(i, 1, N) mark[i] = 0;
    Ford(i, N, 1) {
        if (mark[i]) continue;
        mark[i] = 1;
        ++res;
        Ford(j, i - 1, 1) {
            if (!mark[j] && s[i] + s[j] <= X) {
                mark[j] = 1;
                break;
            }
        }
    }
    printf("%d\n", res);
}

int main() {

#ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
#endif

    cin >> T;
    For(i, 1, T) {
        printf("Case #%d: ", i);
        solve();
    }

}
