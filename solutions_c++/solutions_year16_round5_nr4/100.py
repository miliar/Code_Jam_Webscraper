#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int T, N, L, prob=1;
  for (cin >> T; T--;) {
    cin >> N >> L;
    vector<string> G(N);
    for (int i = 0; i < N; i++) cin >> G[i];
    string B;
    cin >> B;
    cout << "Case #" << prob++ << ": ";

    for (int i = 0; i < N; i++) {
      if (G[i] == B) {cout << "IMPOSSIBLE" << endl; goto done;}
    }

    for (int i = 0; i < L; i++) cout << "0?";
    cout << ' ' << (L==1?string(1, '0'):string(L-1, '1')) << endl;

done:;
  }
}
