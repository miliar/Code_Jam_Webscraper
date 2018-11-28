#include <cstdio>

long long a[10000000];
int ac;

int ispalindrome (long long x) {
  char buf[32];
  int l = sprintf (buf, "%lld", x);
  for (int i = 0; i < l; i++)
    if (buf[i] != buf[l - i - 1]) return 0;
  return 1;
}

int lbound (long long t) {
  int l = -1, r = ac;
  while (r - l > 1) {
    int x = (l + r) >> 1;
    if (t < a[x]) r = x; else l = x;
  }
  return l;
}

int main () {
  for (long long i = 1; i <= (int)1e7; i++) {
    if (ispalindrome (i) && ispalindrome (i * i)) {
      a[ac++] = i * i;
    }
  }
  int tn;
  scanf ("%d", &tn);
  for (int t = 1; t <= tn; t++) {
    long long a, b;
    scanf ("%lld%lld", &a, &b);
    printf ("Case #%d: %d\n", t, lbound (b) - lbound (a - 1));
  }
}
