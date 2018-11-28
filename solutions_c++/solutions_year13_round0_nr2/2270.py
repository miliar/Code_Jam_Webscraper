#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <iomanip>
#include <cassert>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back
#define DBG(...) { if(1) fprintf(stderr, __VA_ARGS__); }
#define DBGDO(X) { if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; }

int field[101][101];
int rfield[101][101];
int rowmin[101];
int colmin[101];
#define FAIL do { goto fail; } while(0)

int main() {
    int T, N, M;
    cin >> T;
    FOR (t, 0, T) {
        cin >> N >> M;
        FOR (n, 0, N) {
            FOR (m, 0, M) {
                int x;
                cin >> x;
                field[n][m] = x;
                rfield[m][n] = x;
            }
        }
        //int c = 0;
        FOR (n, 0, N) {
            FOR (m, 0, M) {
                int v = field[n][m];
                bool ok = true;
                FOR (i, 0, M) {
                    //c++;
                    if (field[n][i] > v) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) {
                    ok = true;
                    //c++;
                    FOR (i, 0, N) {
                        if (field[i][m] > v) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (!ok) FAIL;
            }
        }
        //printf("c=%d\n", c);
        printf("Case #%d: YES\n", t+1);
        continue;
        fail:
        printf("Case #%d: NO\n", t+1);
    }
    return 0;
}

