#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int n;

#define MAX 6
char o[MAX][MAX];
char f[MAX][MAX];
bool used[MAX];

bool check() {
  int perm1[5];
  int perm2[5];
  for(int i=0; i<n; i++) {
    perm1[i] = i;
  }

  do {
    for(int i=0; i<n; ++i) {
      perm2[i] = i;
    }
    do {
      memset(used, false, sizeof(used));

      for(int i=0; i<n; i++) {
        int worker = perm1[i];
        for(int j=0; j<n; j++) {
          int machine = perm2[j];
          if (!used[machine] && f[worker][machine]) {
            used[machine] = true;
            goto found;
          }
        }
        return false;
found:;
      }
    } while (next_permutation(perm2, perm2+n));

  } while(next_permutation(perm1, perm1+n));
  return true;
}

int main() {
  ios::sync_with_stdio(0);
  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    cin >> n;

    for (int i = 0; i < n; ++i) {
      cin >> o[i];
    }

    int mncost = n * n;
    for (int msk = 0; msk < (1 << (n * n)); ++msk) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (msk & (1 << (i * n + j))) {
            f[i][j] = 1;
          } else {
            f[i][j] = o[i][j] - '0';
          }
        }
      }
      if (check()) {
        mncost = min(mncost, __builtin_popcount(msk));
      }
    }
    printf("Case #%d: %d\n", cn, mncost);
  }
  return 0;
}
