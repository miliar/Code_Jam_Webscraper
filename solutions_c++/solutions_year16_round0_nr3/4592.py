#include <bits/stdc++.h>

using namespace std;

const int N = 100000010;

int ans[12];
bitset<N> p;
vector <long long> prime;

void sieve() {
  p.set();
  p[0] = false, p[1] = false;
  for (long long i = 2; i < N - 5; i++) {
    if (p[i]) {
      prime.push_back(i);
      for (long long j = i + i; j < N - 5; j += i) {
        p[j] = false;
      }
    }
  }
}

int main() {
  //  sieve();
  cout << "Done" << endl;
  //  freopen("/home/youssef/Downloads/C-small-attempt0.in", "r", stdin);
  freopen("16.out", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    //    printf("Case #%d:\n", tt);
    int n, m;
    scanf("%d %d", &n, &m);
    int r = 1 | (1 << (n - 1));
    int u, found = 0;
    for (int i = 0; i < (1 << (n - 2)); i++) {
      u = r | (i << 1);
      bool ok = false;
      for (int j = 2; j <= 10; j++) {
        ok = false;
        long long x = 1, y = 0;
        for (int k = 0; k < n; k++) {
          if (u & (1 << k)) {
            y += x;
          }
          x *= j;
        }
        for (long long l = 3; l * l <= y; l += 2) {
          if (y % l == 0) {
            ok = true;
            ans[j] = l;
            break;
          }
        }
        if (y % 2 == 0) {
          ok = true;
          ans[j] = 2;
        }
        if (ok == false) {
          break;
        }
      }
      if (ok) {
        found++;
        for (int l = n - 1; l >= 0; l--) {
          if (u & (1 << l)) {
            printf("1");
          } else {
            printf("0");
          }
        }
        printf(" ");
        for (int l = 2; l <= 9; l++) {
          printf("%d ", ans[l]);
        }
        printf("%d\n", ans[10]);
      }
      if (found == m) {
        break;
      }
    }
  }
  return 0;
}
