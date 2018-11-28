#include <iostream>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  
  int T;
  cin >> T;
  
  for (int ti = 0; ti < T; ++ti) {
    int N;
    cin >> N;
    int P[N];
    for (int i = 0; i < N; ++i) {
      cin >> P[i];
    }
    cout << "Case #" << ti+1 << ": ";
    bool even = 1;
    for(;;) {
      int m = 0, mi, ones = 0;
      for (int i = 0; i < N; ++i) {
        if (P[i] > m) m = P[i], mi = i;
        if (P[i] == 1) ones++;
      }
      if(m==0) break;
      if(m == 1 && ones == 3) even = 0;
      char res = 'A'+mi;
      cout << res << (even ? "" : " ");
      even = !even;
      P[mi]--;
    }
    cout << endl;
  }
}
