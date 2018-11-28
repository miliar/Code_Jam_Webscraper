#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#define MAX 128
int s[MAX][MAX];
int N,M;
char resp[2][8] = {"NO", "YES"};

int main(void)
{
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    printf("Case #%d: ", caso);

    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++)
      for(int j = 0; j < M; j++)
        scanf("%d", &s[i][j]);

    int r = 1;

    for(int i = 0; i < N && r; i++)
      for(int j = 0; j < M && r; j++)
      {
        int ok = 1;
        for(int y = i-1; y >= 0 && ok; y--)
          if (s[i][j] < s[y][j])
            ok = 0;
        for(int y = i+1; y < N && ok; y++)
          if (s[i][j] < s[y][j])
            ok = 0;

        if (ok) continue;

        ok = 1;
        for(int x = j-1; x >= 0 && ok; x--)
          if (s[i][j] < s[i][x])
            ok = 0;
        for(int x = j+1; x < M && ok; x++)
          if (s[i][j] < s[i][x])
            ok = 0;

        if (ok) continue;

        r = 0;
      }

    printf("%s\n", resp[r]);
  }
}
