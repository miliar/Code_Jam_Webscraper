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

using namespace std;

typedef pair<int, int> pi;
typedef pair<int, char> pc;
typedef long long ll;
typedef pair<ll, ll> pl;
typedef pair<string, string> ps;

ps arr[128];

int occ[128];
int occT[128];

string solve(string match, int d) {
  if (d == 1) {
    if (occ[match[0]] == 0 || occ[match[1]] == 0) return "[";
    --occ[match[0]];
    --occ[match[1]];
    if (match[0] > match[1]) swap(match[0], match[1]);
    return match;
  }
  string A = solve(arr[match[0]].first, d - 1);
  string B = solve(arr[match[1]].first, d - 1);
  if (A == "[" || B == "[") return "[";
  if (A > B) swap(A, B);
  return A + B;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("in.in", "r", stdin);
  freopen("in.out", "w", stdout);
#endif

  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int T, n;
  pi A[3];
  cin >> T;
  arr['R'] = ps("RS", "");
  arr['P'] = ps("PR", "");
  arr['S'] = ps("SP", "");

  for (int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ": ";

    cin >> n >> occT['R'] >> occT['P'] >> occT['S'];

    memcpy(occ, occT, sizeof occT); string A = solve(arr['R'].first, n);
    memcpy(occ, occT, sizeof occT); string B = solve(arr['P'].first, n);
    memcpy(occ, occT, sizeof occT); string C = solve(arr['S'].first, n);

    string res = min(A, min(B, C));

    if (res == "[") res = "IMPOSSIBLE";

    cout << res << endl;

  }

  return 0;
}
