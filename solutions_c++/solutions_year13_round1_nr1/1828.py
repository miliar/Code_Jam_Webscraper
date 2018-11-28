#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

int main() {
  int T;
  FILE *fp = fopen("A-small-attempt0.in", "r");
  FILE *fq = fopen("A-small-attempt0.txt", "w");
  fscanf(fp, "%d", &T);
  for(int i = 1; i <= T; i ++) {
    double r, t;
    long long ans;
    fscanf(fp, "%lf%lf", &r, &t);
    ans = (1 - 2 * r + sqrt((2 * r - 1) * (2 * r - 1) + 8 * t)) / 4;
    fprintf(fq, "Case #%d: %lld\n", i, ans);
  }
  fclose(fp);
  fclose(fq);
  return 0;
}
