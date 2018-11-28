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

pii tt[1100];
int n, a[1100], res, pos[1100], b[1100], c[1100], dd[1100];


void check() {
    int dem1 = 0, dem2 = 0;
    FOR(i, 1, n) if (dd[i] == 1) b[++dem1] = a[i];
    FOR(i, 1, n) if (dd[i] == 2) c[++dem2] = a[i];
    sort(b + 1, b + dem1 + 1);
    sort(c + 1, c + dem2 + 1);
    b[++dem1] = n;
    REP(i, dem2, 1) b[++dem1] = c[i];
    FOR(i, 1, n) c[b[i]] = i;
    int sum = 0;
    FOR(i, 1, n) FOR(j, i + 1, n) if (i != j) {
        int x, y;
        if (pos[i] > pos[j]) x = 1; else x = 0;
        if (c[i] > c[j]) y = 1; else y = 0;
        if (x != y) sum++;
    }

    res = min(res, sum);
   // if (sum == 5) {FOR(i, 1, n) cout << b[i] << ' '; cout << endl;}
}

void CAL(int i) {
    if (i == n + 1) check(); else {
        if (a[i] == n) CAL(i + 1); else {
        dd[i] = 1;
        CAL(i + 1);
        dd[i] = 2;
        CAL(i + 1);
        dd[i] = 0;
        }
    }
}

void solve() {
    // init
    FOR(i, 1, n) {
        tt[i].fi = a[i];
        tt[i].sd = i;
    }
    sort(tt + 1, tt + n + 1);
    FOR(i, 1, n) {
        a[tt[i].sd] = i;
        pos[i] = tt[i].sd;
    }

    res = 1000000000;
    FOR(i, 1, n) dd[i] = 0;
    CAL(1);
    cout << res << endl;

}


int main() {
    freopen("round2_B-small-attempt2.in","r",stdin);
    freopen("ans.out","w",stdout);
    int T;
    cin >> T;
    FOR(t, 1, T) {
        cin >> n;
        FOR(i, 1, n) cin >> a[i];
        cout << "Case #" << t << ": ";
        solve();
    }
     return 0;
}
