#include<cstdio>
#include<cstring>

long long sp[1000];
int tot = 0;

int pal (long long num) {
  int d[100];
  int t = 0;
  while (num > 0) {
    d[t ++] = num % 10;
    num /= 10;
  }
  for (int i = 0; i < t - i - 1; i++) {
     if (d[i] != d[t - i - 1]) {
       return false;
     }
  }
  return true;
}

int solve () {
  tot = 0;
  for (long long i = 1; i * i <= 100000000000000LL; i++) {
    if (!pal(i)) continue;
    if (!pal(i * i)) continue;
    sp[tot ++] = i;
  }
}

int Solve (long long L) {
  int ret = 0;
  for (int i = 0; i < tot; i++) {
    if (sp[i] * sp[i] <= L) ret ++; else return ret;
  }
  return ret;
}

int main () {
  freopen ("in.txt", "r", stdin);
  freopen ("ou.txt", "w", stdout);

  solve ();

  int T;
  long long A, B;
  scanf ("%d", &T);
  for (int i = 1; i <= T; i++) {
     printf ("Case #%d: ", i);
     scanf ("%llu%llu", &A, &B);
     printf ("%d\n", Solve (B) - Solve(A - 1));
  }

  return 0;
}
