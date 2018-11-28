#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int infinity = 1e9 + 9;

int R, C;
char M[109][109];
int imp[109][109];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%d %d", &R, &C);
    for (int r = 0; r < R; ++r)
      for (int c = 0; c < C; ++c) {
        scanf(" %c", &M[r][c]);
        imp[r][c] = 0;  // number of disallowed directions
      }
    
    // count and process
    int changes = 0;
    
    // from UP
    for (int c = 0; c < C; ++c) {
      int r = 0;
      while ((r < R) && (M[r][c] == '.')) r++;
      if (r < R) {
        imp[r][c]++;
        //printf("Clash from UP\n");
        if (M[r][c] == '^')
          changes++;
      }
    }
    // from DOWN
    for (int c = 0; c < C; ++c) {
      int r = R - 1;
      while ((r >= 0) && (M[r][c] == '.')) r--;
      if (r >= 0) {
        imp[r][c]++;
        //printf("Clash from DOWN\n");
        if (M[r][c] == 'v')
          changes++;
      }
    }
    // from LEFT
    for (int r = 0; r < R; ++r) {
      int c = 0;
      while ((c < C) && (M[r][c] == '.')) c++;
      if (c < C) {
        imp[r][c]++;
        if (M[r][c] == '<')
          changes++;
      }
    }
    // from RIGHT
    for (int r = 0; r < R; ++r) {
      int c = C - 1;
      while ((c >= 0) && (M[r][c] == '.')) c--;
      if (c >= 0) {
        imp[r][c]++;
        if (M[r][c] == '>')
          changes++;
      }
    }
    
    /*
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c)
        printf("%c", M[r][c]);
      printf("\n");
    }
    */
    
    // impossible?
    bool impossible = false;
    for (int r = 0; r < R; ++r)
      for (int c = 0; c < C; ++c)
        if (imp[r][c] == 4)
          impossible = true;
     
    // output
    if (impossible)
      printf("Case #%d: IMPOSSIBLE\n", Ti);
    else
      printf("Case #%d: %d\n", Ti, changes);
  }
  return 0;
}
