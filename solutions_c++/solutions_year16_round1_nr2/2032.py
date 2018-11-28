#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

void Work(int m, int n, int pos, vector<int>& ans, int a[][50]) {
  int f[300];
  f[0] = 0;
  for (int i = 0; i < m; i++) { f[++f[0]] = a[i][pos]; }
  sort(f + 1, f + 1 + f[0]);
  if ((pos * 2 < m - 1) && (f[pos * 2 + 1] == f[pos * 2 + 2])) { return; }
  int b[3000];
  memset(b, 0, sizeof(b));
  b[f[pos * 2 + 1]] = 1;
  for (int i = 0; i < m; i++) {
     b[a[i][pos]]++;
     if (a[i][pos] == f[pos * 2 + 1]) {
        for (int j = 0; j < n; j++) { b[a[i][j]]--; }
     }
  }
  for (int i = 0; i < 3000; i++)
  if (b[i]) { ans.push_back(i); }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        int n;
        scanf("%d", &n);
        int a[200][50];
        for (int i = 0; i < n * 2 - 1; i++)
            for (int j = 0; j < n; j++) { scanf("%d", &a[i][j]); }
        vector<int> ans(0, 0);
        for (int i = 0; i < n; i++)
        if (ans.size() == 0) { Work(n * 2 - 1, n, i, ans, a); }

        printf("Case #%d:", t);
        for (int i = 0; i < n; i++)
        if (ans[i]) { printf(" %d", ans[i]); }
        printf("\n");
    }
    return 0;
}
