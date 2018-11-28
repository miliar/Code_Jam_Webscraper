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

bool revisa(bool v[]) {
    FOR(i, 0, 10) {
        if (!v[i])
            return false;
    }
    return true;
}

ll solve(ll n) {
    if (!n) return -1;

    bool v[10];
    memset(v, 0, sizeof(v));

    ll it = 1;
    ll act = 0;

    while(!revisa(v)) {
        act = n * it;

        while(act) {
            int dig = act % 10;
            v[dig] = true;
            act /= 10;
        }
        act = n * it;
        it ++;
    }
    return act;
}

int main(){ _
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T;
    ll n;
    cin >> T;

    FOR(t, 1, T+1) {
        cin >> n;
        ll ans = solve(n);
        if (ans == -1) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
        }
        else {
            cout << "Case #" << t << ": " << ans << endl;
        }
    }



    return 0;
}

