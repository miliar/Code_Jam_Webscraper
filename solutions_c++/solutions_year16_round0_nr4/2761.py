#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef long long ll;
typedef unsigned long long ull;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))

#define INF 0x3f3f3f3f
#define MAX -1

#define DEBUG false
#define debug(x) if (DEBUG) cout << #x << " = (" << x << ")\n"

int main() {
    ios::sync_with_stdio(false);

    int T; cin >> T;

    for (int t = 0; t < T; ++t) {
        int K, C, S; cin >> K >> C >> S;

        cout << "Case #" << t+1 << ":";

        ll pot = 1;

        while (--C) pot *= K;

        for (ll i = 1; i <= pot*K; i += pot) {
            cout << " " << i;
        }
        cout << endl;
    }

    return 0;
}
