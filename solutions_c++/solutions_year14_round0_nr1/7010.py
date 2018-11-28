#include <cstdio>
#include <algorithm>

using namespace std;

int c[20];

inline void ff () {
  int a;
  scanf ("%d", &a);
  for (int i = 1;i <= 4;i ++) {
    for (int j = 1;j <= 4;j ++) {
      int x;
      scanf ("%d", &x);
      if (i == a) {
	c[x] ++;
      }
    }
  }
}

inline void solve () {
  for (int i = 1;i <= 16;i ++) {
    c[i] = 0;
  }

  ff ();
  ff ();

  int cnt = 0,ans;
  for (int i = 1;i <= 16;i ++) {
    if (c[i] == 2) {
      cnt ++;
      ans = i;
    }
  }
  if (cnt == 0) {
    printf ("Volunteer cheated!\n");
  } else if (cnt == 1) {
    printf ("%d\n", ans);
  } else {
    printf ("Bad magician!\n");
  }
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d: ", i);
    solve ();
  }
}
