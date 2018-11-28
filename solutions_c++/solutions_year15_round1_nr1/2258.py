#include <iostream>
using namespace std;

int main() {
  int T, N;
  cin >> T;
  int m[10001];

  for (int k=1; k<=T; ++k) {
    cin >> N;
    int ans1 = 0, ans2 = 0, max = 0;
    for (int i=0; i<N; ++i) {
      cin >> m[i];
      if ( i>0 && m[i] < m[i-1]) {
        ans1 += (m[i-1] - m[i]);
        if ((m[i-1] - m[i]) > max) {
          max = (m[i-1] - m[i]);
        }
      }
    }
    for (int i=0; i<N-1; ++i) {
      if (m[i] < max) {
        ans2 += m[i];
      } else {
        ans2 +=max;
      }
    }

    cout << "Case #" << k << ": " << ans1 << " " << ans2 << endl;
  }
  return 0;
}
