#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cassert>

using namespace std;
typedef long long ll;
const int MAXS = 1000;

int main() {
  int T, smax;
  cin >> T;
  string shy;

  for(int t = 1; t <= T; ++t) {
    cin >> smax >> shy;

    assert(shy.length() == smax+1);

    int ans = 0, n_standing = 0;
    for(int lv = 0; lv <= smax; ++lv) {
      int s = shy[lv] - '0';  // #people with shyness lv
      if(n_standing >= lv) n_standing += s;
      else {
        ans += lv - n_standing;  // need lv - n_standing people of shyness 0
        n_standing = s + lv;
      }
    }

    cout << "Case #" << t << ": " << ans;
    if(t < T) cout << "\n";
  }

  return 0;
}
