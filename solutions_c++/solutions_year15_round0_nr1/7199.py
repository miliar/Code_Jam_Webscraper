#include <cstdio>

int T, Smax;
char S[1100];
int friends, standingUp;

int main () {

  freopen("A-large.in", "rt", stdin);
  freopen("output.out", "wt", stdout);

  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    friends = 0;
    standingUp = 0;

    scanf("%d %s", &Smax, S);
    for (int k=0; k<=Smax; ++k) {
      if (standingUp < k) {
	friends += k - standingUp;
	standingUp += k - standingUp;
      }
      standingUp += S[k] - '0';
    }
    printf("Case #%d: %d\n", test, friends);
  }

  return 0;
}
