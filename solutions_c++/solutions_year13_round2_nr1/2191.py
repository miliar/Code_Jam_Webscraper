#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

typedef vector <   int  > vi;
typedef vector <   vi   > vvi;
typedef vector < double > vd;
typedef vector <   vd   > vvd;
typedef vector < string > vs;

int solve (int a, int n, vector<int>& motes) {
  if (n == motes.size())
    return 0;

  if (a == 1)
    return 1 + solve (a, n + 1, motes);

  if (a > motes[n]) {
    a += motes[n];
    return solve (a, n + 1, motes);
  }

  return 1 + min(solve(2 * a - 1, n, motes), solve(a, n + 1, motes));
}

int main () {
  int n, T; cin >> T;

  for (int t = 1; t <= T; t++) {
    int a, n; cin >> a >> n;
    vector<int> motes (n);
    for (int i = 0; i < n; i++)
      cin >> motes[i];

    sort(motes.begin(), motes.end());

    int ans;
    if (a != 1)
      ans = solve(a, 0, motes);
    else
      ans = n;

    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;
}
