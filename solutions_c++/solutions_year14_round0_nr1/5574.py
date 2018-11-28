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

int T, Q, cards[4][4];

int main() {
  cin >> T;
  FOR(cs, 1, T+1) {
    set<int> S;
    cin >> Q;
    FOR(i, 0, 4) FOR(j, 0, 4) cin >> cards[i][j];
    FOR(i, 0, 4) S.insert(cards[Q-1][i]);
    cin >> Q;
    FOR(i, 0, 4) FOR(j, 0, 4) cin >> cards[i][j];
    int res = -1, cnt = 0;
    FOR(i, 0, 4) {
      int v = cards[Q-1][i];
      if (S.find(v) != S.end()) {
        cnt++;
        res = v;
      }
    }
    cout << "Case #" << cs << ": ";
    if (cnt == 0) {
      cout << "Volunteer cheated!" << endl;
    } else if (cnt == 1) {
      cout << res << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
	return 0;
}
