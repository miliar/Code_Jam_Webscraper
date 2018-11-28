// Authored by dolphinigle

#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define INF 1023123123
#define EPS 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define FORIT(X,Y) for(__typeof__((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

int Brute(vector<int> a, bool isshow=false) {
  vector<int> pos(SZ(a), 0);
  vector<int> b = a;
  vector<int> resbest;
  FORN(i, SZ(a)) pos[a[i]] = i;
  sort(ALL(b));
  int best = INF;
  do {
    int updo = 0;
    int ok = 1;
    for (int i = 1; i < SZ(a)-1; ++i) {
      if (b[i] > b[i-1] && b[i] > b[i+1]) {
        updo += 1;
      }
      if (b[i] < b[i-1] && b[i] < b[i+1]) {
        ok = 0;
      }
    }
    if (ok && updo <= 1) {
      int coba = 0;
      FORN(i, SZ(a)) coba += abs(i - pos[b[i]]);
      coba /= 2;
      if (best > coba) {
        best = coba;
        resbest = b;
      }
    }
  } while (next_permutation(ALL(b)));
  if (isshow) {
    for (auto i: resbest) {
      cout << i << " ";
    }
    cout << endl;
  }
  return best;
}

//O(n log n)
vector<int> SequenceSimplify(vector<int> seq) {
	int lowest = 0;
	vector<int> disort = seq;
	sort(ALL(disort));
	disort.erase(unique(ALL(disort)),disort.end());
	FORN(i,SZ(seq)) {
		seq[i] = (lower_bound(ALL(disort),seq[i]) - disort.begin()) + lowest;
		}
	return seq;
	}

//vint a = {10, 50, 5, 50, 10, 70}
//SequenceSimplify(a) = {1, 2, 0, 2, 1, 3}

int stable[1050];

int Calc(vint a) {
  vint res = SequenceSimplify(a);
  int ans = 0;
  FORN(i, SZ(res)) {
    ans += abs(res[i] - i);
  }
  return ans/2;
}

int main() {
  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    printf("Case #%d: ", itc+1);
    int n;
    cin >> n;
    vector<int> res;
    FORN(i, n) {
      int a;
      cin >> a;
      res.PB(a);
      stable[i] = 0;
    }
    res = SequenceSimplify(res);
    int ans = 0;
    vint arq;
    FORN(i, n) arq.PB(res[i]);
    FORN(i, n) {
      int idx = find(ALL(arq), i) - arq.begin();
      ans += min(idx, SZ(arq) - idx - 1);
      arq.erase(arq.begin() + idx);
    }
    cout << ans << endl;
  }
  return 0;
}

