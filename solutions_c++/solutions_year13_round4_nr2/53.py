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

ll T, N, P;

bool sure_to_win(ll team) {
  ll better = team, rank = (1LL << N);
  while (better) {
    rank /= 2;
    better--;
    better /= 2;
  }
  return (1LL << N) - rank + 1 <= P;
}

bool can_win(ll team) {
  ll worse = (1LL << N) - team - 1, rank = (1LL << N);
  while (worse) {
    rank /= 2;
    worse--;
    worse /= 2;
  }
  return rank <= P;
}

int main() {
  cin >> T;
	FOR(cs, 1, T+1) {
    cin >> N >> P;
    ll a = 0, b = (1LL << N) - 1;
    while (a < b) {
      ll m = (a+b+1)/2;
      if (sure_to_win(m)) {
        a = m;
      } else {
        b = m-1;
      }
    }
    ll max_sure = a;
    a = 0, b = (1LL << N) - 1;
    while (a < b) {
      ll m = (a+b+1)/2;
      if (can_win(m)) {
        a = m;
      } else {
        b = m-1;
      }
    }
    ll max_can = a;
    cout << "Case #" << cs << ": " << max_sure << " " << max_can << endl;
	}
	return 0;
}
