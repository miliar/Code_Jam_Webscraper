#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
using namespace std;
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define REP(i,a,b) for(int i=a; i>=b; i--)
#define FORAD(i,u) for(int i=0; i < (int)u.size(),i++)
#define BUG(x) cout << x << endl
#define ll long long
#define fi first
#define sd second
#define pb push_back
#define two(i) 1 << i
#define sz(x) (int)x.size()
#define e 1e-12
#define bit(s,i) ((s >> (i-1)) & 1)
#define Nmax 100100
const double pi = acos(-1);
typedef vector<int> vi ;
typedef pair<int,int> pii ;


int n, res, m, dd[11000], a[11000];

void solve() {
    sort(a + 1, a + n + 1);
    int res = 0;
    FOR(i, 1, n) dd[i] = 0;
    int i = 1, j = n;
    while (i <= j) {
        while (i <= j && dd[i] == 1) i++;
        if (i > j) break;
        while (j >= i && a[i] + a[j] > m) j--;
        dd[i] = dd[j] = 1;
        res++;
        i++;
        j--;
    }
    FOR(i, 1, n) if (dd[i] == 0) res++;
    cout << res << endl;
}

int main() {
     freopen("round2_A-large.in","r",stdin);
     freopen("ans.out","w",stdout);
    int T;
    cin >> T;
    FOR(t, 1, T) {
        cin >> n >> m;
        FOR(i, 1, n) cin >> a[i];
        cout << "Case #" << t << ": ";
        solve();
    }
     return 0;
}
