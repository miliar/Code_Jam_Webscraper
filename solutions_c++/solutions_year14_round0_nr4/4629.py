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

int n;
double naomi[1111], ken[1111];
int naoD, naoW, markK[1111];

void solve() {
    cin >> n;
    For(i, 1, n) cin >> naomi[i];
    For(i, 1, n) cin >> ken[i];
    naoD = naoW = 0;
    sort(naomi + 1, naomi + 1 + n);
    sort(ken + 1, ken + 1 + n);

    int cur = n;
    Ford(i, n, 1) {
        while (cur > 0 && ken[cur] > naomi[i]) --cur;
        if (cur > 0) {
            ++naoD;
            --cur;
        }
    }


    For(i, 1, n) markK[i] = 0;
    Ford(i, n, 1) {
        ++naoW;
        For(j, 1, n)
            if (!markK[j] && ken[j] > naomi[i]) {
                markK[j] = 1;
                --naoW;
                break;
            }
    }

    cout << naoD << " " << naoW;
}

int main() {

#ifndef ONLINE_JUDGE
    freopen("D-large.in", "r", stdin);
    freopen("D.out", "w", stdout);
#endif

    int T;
    cin >> T;
    For(i, 1, T) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }

}
