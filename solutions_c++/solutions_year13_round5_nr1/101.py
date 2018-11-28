#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

typedef long long int LL;

const int SPACES = 37;
const int PAYOUT = 36;

LL reqBudget(int k, LL b, const vector<LL> &bets) {
  LL ret = 0;
  for (int i = 0; i < k; ++i)
    ret += b - bets[i];
  for (int i = k; i < SPACES; ++i)
    if (bets[i] < b+1) ret += b+1 - bets[i];
  return ret;
  }

LL maxAfford(int k, const vector<LL> &bets, LL budget) {
  LL lo = bets[k-1];
  if (reqBudget(k, lo, bets) > budget) return -1;

  LL s = 1, hi = lo + s;
  while (reqBudget(k, hi, bets) <= budget) {
    s <<= 1; hi = lo + s;
    }

  while (hi-lo > 1) {
    LL mid = (hi + lo) / 2;
    if (reqBudget(k, mid, bets) > budget)
      hi = mid;
    else
      lo = mid;
    }

  return lo;
  }

double bestP(int k, const vector<LL> &bets, LL budget) {
  LL b = maxAfford(k, bets, budget);
  if (b < 0) return 0;

  LL stake = 0, extra = 0;
  for (int i = 0; i < k; ++i)
    stake += b - bets[i];
  for (int i = k; i < SPACES; ++i)
    if (bets[i] < b+1) extra += b+1 - bets[i];

  double ret = PAYOUT; ret /= k; ret -= 1;
  ret *= stake; ret -= extra;

  return ret;
  }

int main() {
  cout << fixed << setprecision(8);

  int nc; cin >> nc;
  for (int curC = 1; curC <= nc; ++curC) {
    LL budget; cin >> budget;
    int n; cin >> n;

    vector<LL> bets(SPACES);
    for (int i = 0; i < n; ++i)
      cin >> bets[i];

    sort(bets.begin(), bets.end());

    double ans = 0;
    for (int i = 1; i <= SPACES; ++i)
      ans = max(ans, bestP(i, bets, budget));

    cout << "Case #" << curC << ": " << ans << '\n';
    }
  }

