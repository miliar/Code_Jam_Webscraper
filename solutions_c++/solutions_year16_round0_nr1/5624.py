#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("/home/youssef/Downloads/A-small-attempt0.in", "r", stdin);
  freopen("out.out", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    printf("Case #%d: ", tt);
    int n;
    scanf("%d", &n);
    if (n == 0) {
      puts("INSOMNIA");
      continue;
    }
    long long r = 0, x;
    set <int> st;
    bool ok = false;
    for (int i = 0; i < 10000000; i++) {
      x = r;
      while (x) {
        st.insert(x % 10);
        x /= 10;
      }
      if (st.size() == 10) {
        cout << r << endl;
        ok = true;
        break;
      }
      r += n;
    }
    if (!ok) {
      puts("INSOMNIA");
    }
  }
	return 0;
}
