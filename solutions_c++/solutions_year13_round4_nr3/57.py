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

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, N, A[3000], B[3000], res[3000], indeg[3000];
vi adj[3000];

int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    cin >> N;
    FOR(i, 0, N) cin >> A[i];
    FOR(i, 0, N) cin >> B[i];
    FOR(i, 0, 3000) adj[i].clear();
    FOR(i, 1, N) {
      int last = -1;
      FOR(j, 0, i) {
        if (A[j] >= A[i]) {
          adj[i].push_back(j);
        } else if (A[j] == A[i] - 1) {
          last = j;
        }
      }
      if (last != -1) {
        adj[last].push_back(i);
      }
    }
    FOR(i, 0, N-1) {
      int last = -1;
      FORD(j, i+1, N) {
        if (B[j] >= B[i]) {
          adj[i].push_back(j);
        } else if (B[j] == B[i] - 1) {
          last = j;
        }
      }
      if (last != -1) {
        adj[last].push_back(i);
      }
    }
    memset(indeg, 0, sizeof(indeg));
    FOR(i, 0, N) FOR(j, 0, sz(adj[i])) indeg[adj[i][j]]++;
    FOR(i, 1, N+1) {
      FOR(j, 0, N) {
        if (indeg[j] == 0) {
          FOR(k, 0, sz(adj[j])) indeg[adj[j][k]]--;
          indeg[j] = -1;
          res[j] = i;
          break;
        }
      }
    }
    cout << "Case #" << cs << ":";
    FOR(i, 0, N) cout << " " << res[i];
    cout << endl;
  }
	return 0;
}
