#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <deque>
#include <set>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>

#define left kdjsfkds
#define right dsjlkdflsd
#define pb push_back
#define mp make_pair
#define F first
#define S second

#define foreach(i, c) for (typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

#ifdef LOCAL
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...)
#endif // LOCAL

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long double ld;

const int INF = int(1e9);
const ll INFll = 1ll * INF * INF;
const int MOD = 1000000007;

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif // LOCAL
    int T;
    cin >> T;
    for (int O = 1; O <= T; ++O) {
        cout << "Case #" << O << ": ";
        int n, m;
        cin >> n >> m;
        vector<vector<char> > a(n, vector<char>(m));
        int ans = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> a[i][j];
        bool bad = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (a[i][j] == '.')
                    continue;
                bool up = 0;
                bool down = 0;
                bool left = 0;
                bool right = 0;
                for (int x = i + 1; x < n; ++x)
                    if (a[x][j] != '.')
                        down = 1;
                for (int y = j + 1; y < m; ++y)
                    if (a[i][y] != '.')
                        right = 1;
                for (int y = j - 1; y >= 0; --y)
                    if (a[i][y] != '.')
                        left = 1;
                for (int x = i - 1; x >= 0; --x)
                    if (a[x][j] != '.')
                        up = 1;
                if ((up | left | right | down) == 0)
                    bad = 1;
                if (a[i][j] == '^' && !up || a[i][j] == 'v' && !down || a[i][j] == '<' && !left || a[i][j] == '>' && !right)
                    ans++;

            }
        }
        if (bad)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << endl;
    }
    debug("\nTIME = %ld\n", clock());
    return 0;
}

