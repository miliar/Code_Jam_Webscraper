#include <iostream>
#include <algorithm>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  int T, N;
  cin >> T;
  for (int t=1; t<=T; t++) {
    cout << "Case #" << t << ": ";
    cin >> N;
    char s[4][5];
    for (int i=0; i<N; i++) {
      cin >> s[i];
      for (int j=0; j<N; j++) s[i][j] -= '0';
    }
    int res = N*N;
    for (int i=0; i<(1<<(N*N)); i++) {
      bool fail = false;
      int cost = 0, x[] = {0, 0, 0, 0};
      for (int j=0; j<N; j++) {
        x[j] = (i >> (j*N)) & ((1<<N)-1);
        for (int k=0; k<N && !fail; k++) 
          if (s[j][k] && !(x[j]&(1<<k))) fail = true;
          else if ((x[j]&(1<<k)) && !s[j][k]) cost++;
        if (fail) break;
      }
      if (fail) continue;
      int t[] = {0, 1, 2, 3};
      bool big_fail = false;
      do {
        int p[] = {0, 1, 2, 3};
        do {
          bool fail = false;
          int free = (1<<N)-1;
          for (int k=0; k<N; k++) {
            int a = t[k];
            if ((x[a]&free) == 0) { fail = true; break; }
            if (!(x[a]&(1<<p[k]))) break;
            free ^= (1<<p[k]);
          }
          if (fail) { big_fail = true; break; }
        } while (next_permutation(p, p+N));
        if (big_fail) break;
      } while (next_permutation(t, t+N));
      if (!big_fail) {
        res = min(res, cost);
      }
    }
    cout << res << "\n";
  }
  return 0;
}
