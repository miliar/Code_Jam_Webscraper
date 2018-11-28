#include <iostream>

using namespace std;

#define ull unsigned long long

int main() {
  int T; cin>>T;
  for (int t=1; t <= T; ++t) {
    ull N; cin >> N;

    if (N == 0) {
      printf("Case #%d: INSOMNIA\n", t);
      continue;
    }
    
    bool seen[10];
    for (int i = 0; i < 10; ++i) seen[i] = false;
    ull XN = N;
    while (true) {
      ull temp = XN;
      while (temp != 0) {
        seen[temp%10] = true;
        temp /= 10;
      }
      bool done = true;
      for (int i = 0; i < 10; ++i)
        if (!seen[i]) done = false;
      if (done) break;
      XN += N;
    }
    printf("Case #%d: %lld\n", t, XN);
  }

  return 0;
}
