#include <cstdio>
#include <map>
#include <vector>

using namespace std;

#define Nmax 105

int t, r, c;
map<char, pair<int, int> > Dirs;
char V[Nmax][Nmax];

bool ok(int x, int y) {
  return (x >= 1 && x <= r && y >= 1 && y <= c);
}

int next(int x, int y, char ch) {
   int xx = Dirs[ch].first;
   int yy = Dirs[ch].second;

   while (true) {
      x = x + xx;
      y = y + yy;

      if (!ok(x,y))
        return -1;
      if (V[x][y] != '.')
        return 0;
   }
}

int main() {
  scanf("%d", &t);
  Dirs['^'] = make_pair(-1, 0);
  Dirs['>'] = make_pair(0, 1);
  Dirs['<'] = make_pair(0, -1);
  Dirs['v'] = make_pair(1, 0);

  for (int ti = 1; ti <= t; ++ti) {
    scanf("%d%d", &r, &c);
    int res = 0;

    for (int i = 1; i <= r; ++i)
    for (int j = 1; j <= c; ++j) {
      scanf(" %c", &V[i][j]);
    }

    for (int i = 1; res != -1 && i <= r; ++i)
    for (int j = 1; res != -1 && j <= c; ++j) {
      if (V[i][j] == '.')
        continue;
      
      int dir = next(i, j, V[i][j]);
      if (dir != -1)
        continue;

      ++res;
      if (next(i, j, '>') != -1)
        continue;
      if (next(i, j, '<') != -1)
        continue;
      if (next(i, j, 'v') != -1)
        continue;
      if (next(i, j, '^') != -1)
        continue;

      res = -1;
      printf ("Case #%d: IMPOSSIBLE\n", ti);
    }

    if (res != -1)
      printf("Case #%d: %d\n", ti, res); 
  }
  return 0;
}
