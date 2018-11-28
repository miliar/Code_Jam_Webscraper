#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    int N, X;
    cin >> N >> X;
    vector<int> S(N);
    for (int i = 0; i < N; i++) cin >> S[i];
    sort(S.begin(), S.end());
    int ret = 0;
    for (int i = 0, j = S.size()-1; i <= j; ) {
      ret++;
      if (i == j || S[j] + S[i] > X) {
        j--;
      } else {
        i++; j--;
      }
    }
    cout << "Case #" << prob++ << ": " << ret << endl;
  }
}
