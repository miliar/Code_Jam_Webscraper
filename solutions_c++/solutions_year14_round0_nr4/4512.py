#include <bits/stdc++.h>
using namespace std;

#define ALL(a) a.begin(), a.end()
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORE(i,c) for (int i = 0; i < int((c).size()); ++i)
#define MEM(a,v) memset((a), (v), sizeof(a))
#define SZ(a) int(a.size())
#define pb push_back
#define mp make_pair
#define ft first
#define sd second

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = (1 << 30);
const int MOD = 1000000007;
const double EPS = 1e-7;

vector<double> naomi, ken;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        naomi.clear();
        ken.clear();
        int N;
        cin >> N;
        FOR(i,0,N) {
            double x;
            cin >> x;
            naomi.pb(x);
        }
        FOR(i,0,N) {
            double x;
            cin >> x;
            ken.pb(x);
        }
        sort(ALL(naomi));
        sort(ALL(ken));
        int countW = 0, countDW = 0;
        for (int i = 0, j = 0; i < N; ++i)
            if (naomi[i] > ken[j]) {
                ++j;
                ++countDW;
            }
        for (int i = 0, j = 0; i < N; ++i)
            if (ken[i] > naomi[j]) {
                ++j;
                ++countW;
            }
        countW = N - countW;
        cout << "Case #" << tc << ": " << countDW << " " << countW << "\n";
    }
    return 0;
}