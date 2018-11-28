#include<cstdio>
#include<vector>
#include<cassert>
#include<algorithm>
#define MAXN 13
#define MAX2N 8192
using namespace std;
int sol[MAXN][MAX2N];
int N, val[3];
inline int win(int a, int b) {
  if (a == 0)
    return (b == 1 ? 0 : 2);
  if (a == 1)
    return (b == 2 ? 1 : 0);
  if (a == 2)
    return (b == 0 ? 2 : 1);
  assert(false);
  return -42;
}

bool solve(int i) {
  //printf("enter in %d\n", i);
  if (i >= (1 << N))
    return true;
  for (int v = 0; v < 3; v++) {
    if (!val[v])
      continue;
    sol[0][i] = v;
    val[v]--;
    //printf("%d: i dropped %d\n", i, v);
    int ni = i, row = 0;
    bool ok = true;
    while (ni % 2) {
      if (sol[row][ni] == sol[row][ni-1]) {
        //printf("tie at row %d pos %d\n", row, ni);
        ok = false;
        break;
      }
      assert(win(sol[row][ni], sol[row][ni-1]) == win(sol[row][ni], sol[row][ni-1]));
      sol[row+1][ni/2] = win(sol[row][ni], sol[row][ni-1]);
      ni /= 2;
      row++;
    }
    if (!ok) {
      sol[0][i] = 0;
      val[v]++;
    //printf("i put back %d\n", v);
      continue;
    }
    if (solve(i+1))
      return true;
    sol[0][i] = 0;
    val[v]++;
    //printf("i put back %d\n", v);
  }
  return false;
}
char toc[3] = {'P', 'R', 'S'};
int main() {
  int ncases;
  scanf("%d", &ncases);
  for (int ncase = 0; ncase < ncases; ncase++) {
    scanf("%d%d%d%d", &N, &(val[1]), &(val[0]), &(val[2]));
    printf("Case #%d: ", ncase+1);
    if (!solve(0))
      printf("IMPOSSIBLE\n");
    else {
      for (int i = 0; i < (1 << N); i++)
        putchar(toc[sol[0][i]]);
      putchar('\n');
    }
  }
  return 0;
}
