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

ll dyn[1002][1002]; //a b jml dari a ambil b
int yesinitial = 1;
ll combination(ll people,ll need,ll modu = 1000000007LL * 1000000007LL) {
	if (yesinitial) {
		FORN(i,1002) FORN(j,1002) dyn[i][j] = -1LL;
		yesinitial = 0;
		}
	if (dyn[people][need] != -1LL) return dyn[people][need];
	if (need == 0) return 1LL;
	if (people == need) return 1LL;
	if (people < need) return 0LL;
	dyn[people][need] = combination(people-1,need,modu) + combination(people-1,need-1,modu);
	dyn[people][need] %= modu;
	return dyn[people][need];
	}

ll modu = 1000000007LL;

vector<string> strs;

int wors = 0;
int n;

ll dp[30][121];

pair<int, ll> Solve(int fr, int to, int idx) {
  int hasfront = 0;
  if (SZ(strs[fr]) == idx) {
    hasfront = 1;
    fr += 1;
  }
  int idxbegin = fr;
  vector< pair<int, ll > > rec;
  FORN(i, 26) {
    int idxtail = idxbegin;
    while (idxtail <= to && strs[idxtail][idx] == ('A' + i)) {
      idxtail += 1;
    }
    if (idxtail > idxbegin) {
      rec.PB(Solve(idxbegin, idxtail-1, idx+1));
    }
    idxbegin = idxtail;
  }
  // cout << idxbegin << " " << fr << " " << to << endl;
  // assert(idxbegin == to);
  if (!SZ(rec)) {
    assert(hasfront);
    wors += 1;
    return {1, 1LL};
  }
  if (!hasfront && SZ(rec) == 1) {
    wors += rec[0].A;
    return rec[0];
  }
  // use DP
  FORN(i, SZ(rec)+1) FORN(j, n+1) dp[i][j] = 0;
  dp[0][0] = 1LL;
  FORN(i, SZ(rec)) {
    FORN(j, n+1) if (dp[i][j]) {
      // how many shd allocate to new?
      FORN(k, rec[i].A+1) {
        if (j + k > n) continue;
        int sisa = rec[i].A - k;
        if (j < sisa) continue;
        ll st = dp[i][j];
        (st *= combination(j, sisa)) %= modu;
        (st *= combination(j+k, k)) %= modu;
        (st *= rec[i].B) %= modu;
        (dp[i+1][j+k] += st) %= modu;
      }
    }
  }
  for (int i = n; i >= 1; --i) {
    if (dp[SZ(rec)][i]) {
      if (hasfront) {
        if (i == n) {
          wors += i;
          return {i, (dp[SZ(rec)][i] * (ll)n) % modu};
        } else {
          wors += i+1;
          return {i+1, (dp[SZ(rec)][i] * combination(i+1, 1)) % modu};
        }
      } else {
        wors += i;
        return {i, dp[SZ(rec)][i]};
      }
    }
  }
  assert(false);
  return {0, 0};
}

int Calc(vector<string>& st, int fr, int to, int idx) {
  int hasfront = 0;
  if (SZ(st[fr]) == idx) {
    hasfront = 1;
    fr += 1;
  }
  int ans = 0;
  int idxbegin = fr;
  FORN(i, 26) {
    int idxtail = idxbegin;
    while (idxtail <= to && st[idxtail][idx] == ('A' + i)) {
      idxtail += 1;
    }
    if (idxtail > idxbegin) {
      ans += (Calc(st, idxbegin, idxtail-1, idx+1));
    }
    idxbegin = idxtail;
  }
  if (hasfront) --fr;
  int resto = ans + min(n, to - fr + 1);
  if (SZ(st) == 1) {
  }
  return resto;
}

pair<int, int> Brute(vector<string> strs) {
  int www=0, zzz=0;
  FORN(i, n-1) {
    strs.PB("");
  }
  sort(ALL(strs));
  do {
    vector< vector<string> > uknow;
    uknow.PB({});
    for (auto& i: strs) {
      if (i == "") {
        uknow.PB({});
      } else {
        uknow.back().PB(i);
      }
    }
    int tres = 0;
    int ok = 1;
    for (auto& i: uknow) {
      if (!SZ(i)) {
        ok = 0;
        break;
      }
      tres += Calc(i, 0, SZ(i)-1, 0);
    }
    if (ok) {
      if (tres > www) {
        assert(SZ(uknow) == 3);
        for (auto& i: uknow) {
          for (auto& j: i) {
            cout << j << " ";
          }
          cout << endl;
        }
        www = tres;
        zzz = 0;
      }
      if (tres == www) zzz += 1;
    }
  } while (next_permutation(ALL(strs)));
  return {www, zzz};

}

int main() {
  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    printf("Case #%d: ", itc+1);
    int m;
    cin >> m >> n;
    strs.clear();
    wors = 0;
    FORN(i, m) {
      string x;
      cin >> x;
      strs.PB(x);
    }
    sort(ALL(strs));
    pair<int, ll> x = Solve(0, m-1, 0);
    cout << wors << " " << x.B << endl;
  }
  return 0;
}

