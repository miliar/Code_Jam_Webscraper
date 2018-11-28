#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)

int main() {

  // init_primes();

  // freopen("in.txt", "r", stdin);
  freopen("D-small-attempt0.in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  // ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "CASE #" << i + 1 << ": ";
    int k, c, s;
    cin >> k >> c >> s;
    forn (j, s) {
      cout << j + 1 << ' ';
    }
    cout << endl;
    // string s;
    // cin >> s;
    // cout << solve_fast(s) << endl;
  }

  // solve(32, 50);

  return 0;
}