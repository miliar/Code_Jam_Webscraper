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

string solve(string s) {
    string ret = s.substr(0, 1);
    FOR(i, 1, s.length()) {
        if (ret[0] <= s[i]) {
            ret = s[i] + ret;
        }
        else {
            ret = ret + s[i];
        }
    }
    return ret;
}

int main() { _
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T;
    cin >> T;
    FOR(t, 1, T+1) {
        string s;
        cin >> s;
        cout << "Case #" << t << ": " << solve(s) << endl;
    }
    return 0;
}

