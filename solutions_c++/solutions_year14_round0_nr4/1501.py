#include <stdio.h>
#include <string.h>
#include <algorithm>

using std::sort;

#define MAXN 1005
#define NOTSOLVE -1

int ***decipt;
double naomi[MAXN], ken[MAXN];
int n;

void decipt_init() {
  decipt = new int**[MAXN];
  for (int i = 0; i < MAXN; ++ i) {
    decipt[i] = new int*[MAXN];
    for (int j = 0; j < MAXN; ++ j)
      decipt[i][j] = new int[MAXN];
  }
}

void decipt_clear() {
  for (int i = 0; i < MAXN; ++ i)
    for (int j = 0; j < MAXN; ++ j)
      memset(decipt[i][j], 0xff, sizeof(int) * MAXN);
}

int solve_decipt_war(int i, int j, int k) {
  if (j == k) return naomi[i] > ken[j];
  else if (decipt[i][j][k] != NOTSOLVE) return decipt[i][j][k];
  
  if (naomi[i] < ken[j]) return decipt[i][j][k] = solve_decipt_war(i + 1, j, k - 1);
  if (naomi[i] < ken[k]) { // naomi[i] > ken[j]
    return decipt[i][j][k] = solve_decipt_war(i + 1, j, k - 1) > solve_decipt_war(i + 1, j + 1, k) + 1 ?
      solve_decipt_war(i + 1, j, k - 1) : solve_decipt_war(i + 1, j + 1, k) + 1;
  } else {
    return decipt[i][j][k] = solve_decipt_war(i + 1, j + 1, k) + 1;
  }
}

int find_ken_first(bool kenUsed[]) {
  for (int i = 0; i < n; ++ i)
    if (kenUsed[i] == false) return i;
}

int find_ken_greater(double num, bool kenUsed[]) {
  for (int i = 0; i < n; ++ i)
    if (kenUsed[i] == false && ken[i] > num) return i;
  return -1;
}

int solve_war() {
  bool *kenUsed = new bool[MAXN];
  memset(kenUsed, false, sizeof(bool) * MAXN);
  
  int score = 0;
  for (int i = 0; i < n; ++ i) {
    
    int idx = find_ken_greater(naomi[i], kenUsed);
    if (idx == -1) {
      score ++;
      kenUsed[find_ken_first(kenUsed)] = true;
    } else {
      kenUsed[idx] = true;
    }
  }

  delete []kenUsed;
  return score;
}

int main() {
  int t;
  scanf("%d", &t);
  decipt_init();

  for (int cases = 1; cases <= t; ++ cases) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++ i) scanf("%lf", &naomi[i]);
    for (int i = 0; i < n; ++ i) scanf("%lf", &ken[i]);

    decipt_clear();
    
    sort(naomi, naomi + n);
    sort(ken, ken + n);
    printf("Case #%d: %d %d\n", cases, solve_decipt_war(0, 0, n - 1), solve_war());
  }
  return 0;
}
