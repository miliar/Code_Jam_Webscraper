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

int TC, N, M, P, U[30], V[30], A[30], B[30], C[30], route[20];
int dist1[30], dist2[30];

void calc_dists() {
  memset(dist1, oo, sizeof(dist1));
  dist1[1] = 0;
  FOR(i, 0, N) FOR(j, 1, M+1) {
    dist1[V[j]] = min(dist1[V[j]], dist1[U[j]] + C[j]);
  }
  memset(dist2, oo, sizeof(dist2));
  dist2[2] = 0;
  FOR(i, 0, N) FOR(j, 1, M+1) {
    dist2[U[j]] = min(dist2[U[j]], dist2[V[j]] + C[j]);
  }
}

int main() {
  cin >> TC;
  FOR(cs, 1, TC+1) {
    cin >> N >> M >> P;
    FOR(i, 1, M+1) cin >> U[i] >> V[i] >> A[i] >> B[i];
    FOR(i, 0, P) cin >> route[i];
    int res = -1;
    FOR(i, 0, P) {
      FOR(j, 1, M+1) C[j] = B[j];
      int dst = 0;
      FOR(j, 0, i+1) {
        C[route[j]] = A[route[j]];
        dst += C[route[j]];
      }
      calc_dists();
      bool found = true;
      while (found) {
        found = false;
        FOR(j, 1, M+1) {
          int diff = dist1[U[j]] + C[j] + dist2[V[j]] - dist1[2];
          if (diff <= 0 || C[j] == A[j]) continue;
          C[j] = max(C[j] - diff, A[j]);
          calc_dists();
          found = true;
          break;
        }
      }
      if (dist1[2] < dst + dist2[V[route[i]]]) {
        res = route[i];
        break;
      }
    }
    if (res == -1) {
      cout << "Case #" << cs << ": Looks Good To Me" << endl;
    } else {
      cout << "Case #" << cs << ": " << res << endl;
    }
  }
	return 0;
}
