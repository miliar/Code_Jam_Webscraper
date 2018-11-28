#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

int R, C; 
char grids[104][104];
int dir[102][102];
int e[] = {1, 2, 4, 8};
int all = 15;
char c[200];

int main() { int T, res;
  std::cin >> T;

  c['^'] = e[0];
  c['>'] = e[1];
  c['v'] = e[2];
  c['<'] = e[3];
  for (int n_case = 1; n_case <= T; n_case++) {
    std::cin >> R >> C;
    for (int i = 1; i <= R; i++) 
      std::scanf ("%s", &grids[i][1]);

    for (int i = 1; i < C+2; i++) {
      grids[0][i] = grids[R+1][i] = '.';
      dir[0][i] = e[0];
      dir[R+1][i] = e[2];
    }
    for (int i = 1; i < R+2; i++) {
      grids[i][0] = grids[i][C+1] = '.';
      dir[i][0] = e[3];
      dir[i][C+1] = e[1];
    }

    res = 0;
    for (int x = 1;  x <= C; x++)
      for (int y = 1; y <= R; y++) {
        dir[y][x] = 0;
        if (grids[y][x-1] == '.' && (dir[y][x-1] & e[3]))
          dir[y][x] = e[3];
        if (grids[y-1][x] == '.' && (dir[y-1][x] & e[0]))
          dir[y][x] |= e[0];
      }
    for (int x = C; x >= 1; x--) 
      for (int y = R; y >= 1; y--) {
        if (grids[y+1][x] == '.' && (dir[y+1][x] & e[2]))
          dir[y][x] |= e[2];
        if (grids[y][x+1] == '.' && (dir[y][x+1] & e[1]))
          dir[y][x] |= e[1];
        if (dir[y][x] == all && grids[y][x] != '.') {
          res = -1;
          goto done;
        }
        else if (grids[y][x] != '.' && (dir[y][x] & c[grids[y][x]])) 
          res++;
      }

done:
    std::printf("Case #%d: ", n_case);
    if (res == -1) std::printf ("IMPOSSIBLE\n");
    else std::cout << res << '\n';
  }

  return 0;
}
