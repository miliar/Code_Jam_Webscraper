#include <cstdio>

char bfr[1002];

int doit() {
  int smax;
  int pplSoFar = 0;
  int friendsNeeded = 0;
  scanf("%d", &smax);
  scanf("%s", bfr);
  for (int lvl = 0; lvl <= smax; ++lvl) {
    if (pplSoFar + friendsNeeded < lvl) friendsNeeded++;
    char val = bfr[lvl];
    val -= '0';
    pplSoFar += val;
  }
  return friendsNeeded;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i)
    printf("Case #%d: %d\n", i, doit());
  return 0;
}
