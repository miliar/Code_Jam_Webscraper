#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <stdio.h>
#include <stack>
#include <map>
#include <math.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef vector<int> VI;
typedef vector<VI> VVI;
#define rep(i,n) for (int i=0; i < (n); i++)


ll getLargestGuaranteedToWin(int n, ll p, int depth) {
  ll numTeams = 1LL << n;
  ll width = 1LL << depth;
  ll smallestTeam = (1LL << depth) - 1;
  if (p <= numTeams / 2) return smallestTeam + width - 1;  // yes, you are the promised winner
  return getLargestGuaranteedToWin(n-1, p - numTeams / 2, depth + 1);
}

PLL solve() {
  int n;
  ll p;
  cin >> n >> p;
  ll numTeams = 1LL << n;
  if (numTeams == p) {
    return PLL(numTeams-1, numTeams-1);
  }
  ll largestPromised = getLargestGuaranteedToWin(n, p, 0);
  ll largestPossible = numTeams - 2 - getLargestGuaranteedToWin(n, numTeams - p, 0);

  return PLL(largestPromised, largestPossible);
}

int main() {
  int t;
  cin >> t;
  rep(i, t) {
    PLL ans = solve();
    cout << "Case #" << i+1 << ": " << ans.first << " " << ans.second << endl;
  }
  return 0;
}