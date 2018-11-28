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
int cards[4][4];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        int r1, r2;
        cin >> r1; --r1;
        FOR(i,0,4) FOR(j,0,4) cin >> cards[i][j];
        set<int> s;
        FOR(i,0,4) s.insert(cards[r1][i]);
        cin >> r2; --r2;
        FOR(i,0,4) FOR(j,0,4) cin >> cards[i][j];
        int cnt = 0, crd = 0;
        FOR(i,0,4)
            if (s.count(cards[r2][i])) {
                ++cnt;
                crd = cards[r2][i];
            }
        cout << "Case #" << tc << ": ";
        if (cnt == 0) {
            cout << "Volunteer cheated!\n";
        }
        else if (cnt > 1) {
            cout << "Bad magician!\n";
        }
        else {
            cout << crd << "\n";
        }
    }
    return 0;
}