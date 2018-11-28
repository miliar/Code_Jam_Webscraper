#include <bits/stdc++.h>
using namespace std;
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

int T;

void flip(string &s, int p, int q) {
  for (int i = p; i <= q / 2; i++) {
    swap(s[i], s[q - i]);
  }
  for (int i = p; i <= q; i++) {
    if (s[i] == '+') {
      s[i] = '-';
    } else {
      s[i] = '+';
    }
  }
}

int main() {
#ifdef msci
  //freopen("input.txt", "r", stdin);
#endif
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    fflush(stdout);
    // begin solution
    string s; 
    cin >> s;
    string fn = "";
    for (int i = 0; i < (int) s.size(); i++) {
      fn += '+';
    }
    unsigned long long ans = 0;
    while (s != fn) {
      unsigned long long i = 0;
      while (i < s.size() && s[i] == '+') { i++; }
      if (i > 0) {
        flip(s, 0, i - 1);
        ans++;
      }
      i = 0;
      while (i < s.size() && s[i] == '-') { i++; }
      if (i > 0) {
        flip(s, 0, i - 1);
        ans++;
      }
    }
    cout << ans << "\n";
    fflush(stdout);
    //end solution
  }
  return 0;
}
