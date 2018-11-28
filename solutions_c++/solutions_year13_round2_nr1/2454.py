#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

long long solve(vector<int> &motes, int i, int A) {
  int N = motes.size();
  long long r = 0;
  for (; i < N; ++i) {
    if (motes[i] >= A) {
      long long a = -1, b = -1;
      a = solve(motes, i+1, A) + 1;
      if (A-1 > 0) {
	b = solve(motes, i, 2*A-1) + 1;
      }
      if (a != -1 && b != -1)
	r = min(a, b);
      else if (a != -1)
	r = a;
      else if (b != -1)
	r = b;
      break;
    } else {
      A += motes[i];
    }
  }
  return r;
}


int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    long long A, N, r = 0;
    cin >> A >> N;
    vector<int> motes;
    for (int n = 0; n < N; ++n) {
      int m; cin >> m;
      motes.push_back(m);
    }
    sort(motes.begin(), motes.end());
    r = solve(motes, 0, A);
    printf("Case #%d: %lld\n", t, r);
  }
  return 0;
}
