#define NDEBUG
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

template<typename T, typename U> inline bool makemax(T &res, const U &x) {
  if (x > res) {
    res = x;
    return true;
  }
  return false;
}
#define ZERO(v) memset((v), 0, sizeof (v))
#define ALL(x) (x).begin(), (x).end()

const int MAXN = 205;

vector<double> P_picked;
bool bio[MAXN][MAXN+1];
double memo[MAXN][MAXN+1];

double calc(int pos, int to_vote_yes) {
  if (to_vote_yes < 0) {
    return 0.0;
  }
  if (pos == (int)P_picked.size()) {
    return to_vote_yes == 0 ? 1.0 : 0.0;
  }

  double& ret = memo[pos][to_vote_yes];
  if (bio[pos][to_vote_yes]) {
    return ret;
  }

  bio[pos][to_vote_yes] = true;
  ret =
         P_picked[pos]  * calc(pos+1, to_vote_yes-1) +
    (1.0-P_picked[pos]) * calc(pos+1, to_vote_yes);
  return ret;
}

double solve() {
  int n, K;
  cin >> n >> K;
  vector<double> P(n);
  for (int i=0; i<n; ++i) {
    cin >> P[i];
  }
  sort(ALL(P));

  double ans = 0;
  for (int a=0; a<=K; ++a) {
    P_picked.clear();
    P_picked.insert(P_picked.end(), P.begin(), P.begin() + a);
    P_picked.insert(P_picked.end(), P.end() - (K-a), P.end());
    ZERO(bio);
    makemax(ans, calc(0, K/2));
  }
  return ans;
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    printf("Case #%d: %.9f\n", tt, solve());
    fflush(stdout);
  }
}
