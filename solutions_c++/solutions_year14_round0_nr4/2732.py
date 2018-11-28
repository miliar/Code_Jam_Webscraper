#include <cstdio>
#include <stdlib.h>
using namespace std;

int compare(const void *a, const void *b)
{
    double *pa = (double*)a;
    double *pb = (double*)b;
    if ((*pa) > (*pb)) return 1;
    if ((*pa) < (*pb)) return -1;
    return 0;
}

int main() {
  FILE *fin = fopen("D-large.in", "r");
  FILE *fout = fopen("D-large.out", "w");
  int testnum;
  fscanf(fin, "%d", &testnum);
  for (int test = 1; test <= testnum; ++test) {
    int n = 0;
    double naomi[1005], ken[1005];
    fscanf(fin, "%d", &n);
    for (int i = 0; i < n; ++i) {
      fscanf(fin, "%lf", &naomi[i]);
    }
    for (int i = 0; i < n; ++i) {
      fscanf(fin, "%lf", &ken[i]);
    }
    qsort(naomi, n, sizeof(double), compare);
    qsort(ken, n, sizeof(double), compare);
    /*for (int i = 0; i < n; ++i) {
      printf("%lf, %lf\n", naomi[i], ken[i]);
    }
    printf("-----------------\n");*/
    // Playing deceitful war
    int dscore = 0;
    int kenlast = 0;
    for (int i = 0; i < n; ++i) {
      int j = 0;
      for (j = kenlast; j < n; ++j) {
        if (ken[j] < naomi[i]) {
          ++dscore;
          kenlast = j + 1;
          break;
        } else {
          break;
        }
      }
    }
    // Playing war
    kenlast = 0;
    int wscore = n;
    for (int i = 0; i < n; ++i) {
      int j = 0;
      for (j = kenlast; j < n; ++j) {
        if (ken[j] > naomi[i]) {
          --wscore;
          kenlast = j + 1;
          break;
        }
      }
      if (j == n) {
        break;
      }
    }
    fprintf(fout, "Case #%d: %d %d\n", test, dscore, wscore);
  }
}