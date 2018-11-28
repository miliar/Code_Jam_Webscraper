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

int T, N, A[1100];

int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    cin >> N;
    FOR(i, 0, N) cin >> A[i];
    int a = 0, b = N-1, res = 0;
    while (a < b) {
      int imin = a;
      FOR(i, a+1, b+1) {
        if (A[i] < A[imin]) imin = i;
      }
      if (imin - a < b - imin) {
        res += (imin - a);
        FORD(i, a, imin) swap(A[i], A[i+1]);
        a++;
      } else {
        res += (b - imin);
        FOR(i, imin, b) swap(A[i], A[i+1]);
        b--;
      }
    }
    cout << "Case #" << cs << ": " << res << endl;
  }
	return 0;
}
