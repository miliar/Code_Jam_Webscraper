#include <bits/stdc++.h>
#define BSET(p,n) ((p) |= (1 << (n)))
#define TARGET 0x3ff
#define MAXI 123456
using namespace std;

int64_t calc(int64_t n) {
  if (n==0) return 0;
  int bs = 0;
  int64_t curr;
  for (int i=1; i<=MAXI; i++) {
    curr = n*i;
    while (curr) {
      BSET(bs, curr%10);
      curr /= 10;
    }
    if (bs == TARGET) return n * i;
  }
  return 0;
}

int main() {
  int64_t T, N, ans;
  cin >> T;
  for (int t=1; t<=T;t++) {
    cin >> N;
    ans = calc(N);
    cout << "Case #" << t << ": ";
    if (ans==0) {
      cout << "INSOMNIA" << endl;
    } else {
      cout << ans << endl;
    }
  }
}
