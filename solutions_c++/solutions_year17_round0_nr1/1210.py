#include <bits/stdc++.h>

#define PI 3.14159265358979323846
#define EPS 1e-6
#define INF 1000000000

#define _ ios_base::sync_with_stdio(0), cin.tie(0), cin.tie(0), cout.tie(0), cout.precision(15);
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define RFOR(i, a, b) for(int i=int(a)-1; i>=int(b); i--)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define RFORC(cont, it) for(decltype((cont).rbegin()) it = (cont).rbegin(); it != (cont).rend(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

#define MAXN 1005
#define MOD 1000000007

int k;
string s;
bool arr[MAXN];

string solve() {
    int ans = 0;
    int n = s.length();
    FOR(i, 0, n)    arr[i] = s[i] == '+';

    FOR(i, 0, n-k+1) {
        if (arr[i] == 0) {
            ans ++;
            FOR(j, 0, k) {
                arr[i+j] = !arr[i+j];
            }
        }
    }

    bool b = 1;
    FOR(i, 0, n)    b = b && arr[i] == 1;

    if (!b)  return "IMPOSSIBLE";
    else    return to_string(ans);
}

int main() { _
    int T;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    cin >> T;
    FOR (t, 1, T + 1) {
        cin >> s >> k;

        cout << "Case #" << t << ": " << solve() << endl;
    }



    return 0;
}
