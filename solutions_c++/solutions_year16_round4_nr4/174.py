#include <bits/stdc++.h>
using namespace std;

int t, n;

char c[30][30];
int p[30][30];

int x[30][30];

int check() {
  vector<int> orderworker;
  vector<int> ordermachine;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (x[i][j] < p[i][j]) {
        return 1000000000;
      }
    }
  }
  for (int i = 0; i < n; i++) {
    orderworker.push_back(i);

  }
  do {
    ordermachine.clear();
    for (int i = 0; i < n; i++) {
      ordermachine.push_back(i);
    }
    do {
      vector<bool> used;
      for (int i = 0; i < n; i++) {
        used.push_back(false);
      }
      for (int i = 0; i < n; i++) {
        if (!x[orderworker[i]][ordermachine[i]]) {
          if (orderworker[0] == 0 && ordermachine[0] == 0 && orderworker[1] == 1 && ordermachine[1] == 1) {

          }
          //check if he still has valid options
          bool hasOptions = false;
          for (int j = 0; j < n; j++) {
            if (x[orderworker[i]][j] && !used[j]) {
              hasOptions = true;
            }
          }
          if (!hasOptions) {
            return 1000000000;
          } else {
            break;
          }
        }
        used[ordermachine[i]] = true;
      }
    } while (next_permutation(ordermachine.begin(), ordermachine.end()));
  } while (next_permutation(orderworker.begin(), orderworker.end()));
  int result = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      result += x[i][j] - p[i][j];
    }
  }
  /*
  if (result == 0) {
    printf("!!%d\n", n);

  }*/
  return result;

}

int main() {
  scanf("%d", &t);
  int cs = 0;
  while (t--) {
    ++cs;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%s", c[i]);
      for (int j = 0; j < n; j++) {
        if (c[i][j] == '1') {
          p[i][j] = 1;
        } else {
          p[i][j] = 0;
        }
      }
    }
    int result = 1000000000;
    for (int i = 0; i < (1<<(n*n)); i++) {
      for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
          if (i & (1<<(j * n + k))) {
            x[j][k] = 1;
          } else {
            x[j][k] = 0;
          }
        }
      }
      result = min(result, check());
    }
    printf("Case #%d: ", cs);
    printf("%d\n", result);
  }
}
