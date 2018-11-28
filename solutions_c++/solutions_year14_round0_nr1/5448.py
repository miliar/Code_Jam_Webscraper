#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int MaxN = 20;

int r1[MaxN], r2[MaxN];

void solve (int tc) {
  int R1, R2;
  scanf("%d",&R1);
  --R1;
  for (int r = 0; r < 4; ++r)
    for (int c = 0; c < 4; ++c) {
      int x;
      scanf("%d",&x);
      r1[x] = r;
    }
  scanf("%d",&R2);
  --R2;
  for (int r = 0; r < 4; ++r)
    for (int c = 0; c < 4; ++c) {
      int x;
      scanf("%d",&x);
      r2[x] = r;
    }

  int sol = -1;

  printf("Case #%d: ",tc);

  for (int x = 1; x <= 16; ++x) {
    if (r1[x] != R1 || r2[x] != R2)
      continue;
    if (sol != -1) { 
      printf("Bad magician!\n");
      return;
    }
    sol = x;
  }

  if (sol == -1)
    printf("Volunteer cheated!\n");
  else
    printf("%d\n",sol);
}

int main (void) {
  int t;
  scanf("%d",&t);
  for (int c = 1; c <= t; ++c)
    solve(c);
  return 0;
}
