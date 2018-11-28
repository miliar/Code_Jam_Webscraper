#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define f(x, y) for(int x = 0; x < (int)y; ++x)

typedef vector<int> vi;
typedef vector<bool> vb;

int solve() {
  int N, X; cin >> N >> X;
  vi v(N);
  f(i, N) cin >> v[i];
  sort(v.begin(), v.end());
  vb s(N, false);
  int r = 0;
  f(i, N) if (!s[i]) {
    s[i] = true;
    ++r;
    int j = upper_bound(v.begin(), v.end(), X-v[i])-v.begin();
    while (--j >= 0 && s[j]);
    if (j>=0) s[j] = true;
  }
  return r;
}

int main() {
  int T; cin >> T;
  for (int C = 1; C <= T; ++C) {
    cout << "Case #" << C << ": " << solve() << endl;
  }
}
