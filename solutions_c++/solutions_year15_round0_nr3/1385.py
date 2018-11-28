#include <cstdio>
#include <cstring>

#define Nmax (1<<17)

const int qua[8][8] = {
  {0, 1, 2, 3, 4, 5, 6, 7},
  {1, 4, 3, 6, 5, 0, 7, 2},
  {2, 7, 4, 1, 6, 3, 0, 5},
  {3, 2, 5, 4, 7, 6, 1, 0},
  {4, 5, 6, 7, 0, 1, 2, 3},
  {5, 0, 7, 2, 1, 4, 3, 6},
  {6, 3, 0, 5, 2, 7, 4, 1},
  {7, 6, 1, 0, 3, 2, 5, 4}
};

int t,x,n;
char V[Nmax];
bool mark[2][Nmax];

inline int repr(char c) {
  return (c == 'i' ? 1 : (c == 'j' ? 2 : 3));
}

inline char nrepr(int c) {
  return (c == 1 ? 'i' : (c == 2 ? 'j' : 'k'));
}

void print(int k, int a, int b) {
  printf ("Found for %c: ", (k == 0) ? 'i' : 'k');
  for (int i = a; i <= b; ++i)
    printf("%c", nrepr(V[i % n]));
  printf("\n"); 
}

bool solve() {
  memset(mark, 0, sizeof(mark));

  int cm = 0;
  for (int i = 0; i < n * x; ++i) {
    cm = qua[cm][ V[i % n] ];
    if (cm == 1) {
      //print(0, 0, i);
      mark[0][i] = true;
    }
  }

  cm = 0;
  for (int i = n * x - 1; i >= 0; --i) {
    cm = qua[ V[i % n] ][cm];
    if (cm == 3) {
      //print(1, i, n * x - 1);
      mark[1][i] = true;
    }
  }

  for (int i = 0; i < n * x; ++i) {
    if (!mark[0][i])
      continue;

    cm = 0;
    for (int j = i + 1; j < n * x; ++j) {
      cm = qua[cm][ V[j % n] ];
      if (cm == 2 && mark[1][j + 1])
        return true;
    } 
  }
  return false;
}

int main() {
  scanf("%d", &t);
  for (int ti = 1; ti <= t; ++ti) {
    scanf("%d%d\n", &n, &x);
    char c;
    for (int i = 0; i < n; ++i) {
      scanf(" %c", &c);
      V[i] = repr(c);
    }
    bool ok = solve();
    if (ok)
      printf("Case #%d: YES\n", ti);
    else
      printf("Case #%d: NO\n", ti);
  }

  return 0;
}
