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

int T, P, Q, N, H[200];
ll G[200], tab[200][2000];

ll rek(int pos, int sh) {
  if (pos >= N) return 0;
  ll& res = tab[pos][sh];
  if (res != -1) return res;
  res = rek(pos+1, sh+((H[pos]+Q-1)/Q));
  FOR(p, 0, 11) FOR(q, 0, 11) {
    if (p - q + 1 > sh) continue;
    int sh2 = sh - (p - q + 1);
    int rem = H[pos] - p * P - q * Q;
    if (rem <= 0 || rem > P) continue;
    res = max(res, G[pos] + rek(pos+1, sh2));
  }
  return res;
}

int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    cin >> P >> Q >> N;
    FOR(i, 0, N) cin >> H[i] >> G[i];
    memset(tab, -1, sizeof(tab));
    cout << "Case #" << cs << ": " << rek(0, 1) << endl;
  }
	return 0;
}
