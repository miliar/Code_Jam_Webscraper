#include <cstdio>

#define N 4 //20 man
int a[N][N], b[N][N];

void Solve() {
   int rowA, rowB;
   scanf("%d", &rowA); rowA--;
   for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
         scanf("%d", a[i] + j);
      }
   }
   scanf("%d", &rowB); rowB--;
   for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
         scanf("%d", b[i] + j);
      }
   }
   int sol = -1, nrEq = 0;
   for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
         if (a[rowA][i] == b[rowB][j]) {
            sol = a[rowA][i];
            nrEq++;
         }
      }
   }
   if (nrEq == 0) {
      printf("Volunteer cheated!\n");
      return;
   }
   if (nrEq > 1) {
      printf("Bad magician!\n");
      return;
   }
   printf("%d\n", sol);
}

int main() {
   freopen("data.in", "rb", stdin);
   freopen("data.out", "wb", stdout);
   int tst;
   scanf("%d", &tst);
   for (int i = 1; i <= tst; i++) {
      printf("Case #%d: ", i);
      Solve();
   }
}