#include <bits/stdc++.h>

#define PI 3.141592653589793
#define EPS 0.000000001
#define INF 1000000000

#define _ ios_base::sync_with_stdio(0), cin.tie(0), cin.tie(0), cout.tie(0), cout.precision(15);
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define MAXN 10
#define MOD 1000000007

vi v;
int total, n;

void solve1() {
    int maxi = 0;

    FOR(i, 0, n) {
        if (v[i] > v[maxi]) {
            maxi = i;
        }
    }
    v[maxi] --;
    char c = 'A' + maxi;
    cout << c;
    total --;
}

void solve() {
    while (total) {
        solve1();
        if (total != 2) {
            solve1();
        }
        cout << " \n"[!total];
    }
}

int main(){ _
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T, a;
    cin >> T;
    FOR(t, 1, T+1) {
        v.clear();
        total = 0;

        cin >> n;
        FOR(i, 0, n) {
            cin >> a;
            v.pb(a);
            total += a;
        }
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
