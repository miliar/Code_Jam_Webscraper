#include <iostream>
#define MAXN 1001

using namespace std;

int n;
int A[MAXN];

int solve() {
  int ans = MAXN;
  for (int i = 1; i < MAXN; ++i) {
    int q = i;
    for (int j = 0; j < n; ++j)
      q += (A[j] + i - 1) / i - 1;
    ans = min(ans, q);
  }
  return ans;
}

int main() {
  ios::sync_with_stdio(0);
  int tc;
  cin >> tc;
  for (int i = 0; i < tc; ++i) {
    cin >> n;
    for (int j = 0; j < n; ++j)
      cin >> A[j];
    cout << "Case #" << i + 1 << ": ";
    cout << solve() << endl;
  }
  return 0;
}
