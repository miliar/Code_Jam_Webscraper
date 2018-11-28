#include <cstdio>
#include <algorithm>

using namespace std;

int R, C, M;
char m[5*5], sol[5*5];
int rem;

inline int a(int y, int x) { return y*C+x; }
bool outside(int y, int x) { return (y < 0 || y >= R || 0 > x || x >= C); }

int hasmine(int y, int x) {
  return outside(y, x) ? 0 : m[a(y,x)] == '*';
}

int nmines(int y, int x) {
  int s = 0;
  for (int dy = -1; dy <= 1; dy++)
    for (int dx = -1; dx <= 1; dx++)
      s += hasmine(y+dy,x+dx);
  return s;
}

void ff(int y, int x) {
  if (outside(y, x))
    return;
  if (sol[a(y, x)] != '.')
    return;
  int n = nmines(y, x);
  sol[a(y, x)] = '0' + n;
  rem--;
  if (!n) {
    for (int dy = -1; dy <= 1; dy++)
      for (int dx = -1; dx <= 1; dx++)
        ff(y+dy, x+dx);
  }
}

void print(char m[]) {
  for (int y = 0; y < R; y++) {
    for (int x = 0; x < C; x++)
      putchar(m[a(y,x)]);
    putchar('\n');
  }
}

bool go() {
  int cx, cy;
  rem = R*C-M;
  for (int y = 0; y < R; y++)
    for (int x = 0; x < C; x++)
      if ((sol[a(y,x)] = m[a(y,x)]) == 'c') {
        cx = x;
        cy = y;
        sol[a(y,x)] = '.';
      }
  ff(cy, cx);
  //  printf("%d %d -> %d\n", cy, cx, rem);
  //  print(sol);
  return !rem;    
}

int main() {

  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d%d", &R, &C, &M);
    printf("Case #%d:\n", t);
    int S = R*C;
    for (int i = 0; i < S; i++)
      m[i] = i < M ? '*' : (i == M ? 'c' : '.');
    sort(m, m + S);
    bool solved = false;
    do
      solved = go();
    while (!solved && next_permutation(m, m+S));
    if (solved) {
      print(m);
    } else
      puts("Impossible");
  }

  return 0;
}
