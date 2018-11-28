#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int r[2];
int table[2][20][20];

void ReadData()
{
  for(int T = 0; T < 2; T++)
  {
    scanf("%d", &r[T]);
    for(int i = 0; i < 4; i++)
    {
      for(int j = 0; j < 4; j++)
      {
        scanf("%d", &table[T][i][j]);
      }
    }
  }
}

bool used[2][29];

void Solve()
{
  memset(used, 0, sizeof(used));
  for(int T = 0; T < 2; T++)
  {
    for(int j = 0; j < 4; j++)
    {
      int num = table[T][r[T] - 1][j];
      used[T][num] = true;
    }
  }
  int answer = -1;
  for(int i = 1; i < 17; i++)
  {
    if(used[0][i] && used[1][i])
    {
      if(answer == -1)
      {
        answer = i;
      }
      else
      {
        printf("Bad magician!\n");
        return;
      }
    }
  }
  if(answer == -1)
  {
    printf("Volunteer cheated!\n");
  }
  else
  {
    printf("%d\n", answer);
  }
}

int main()
{
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int QWE;
  scanf("%d", &QWE);
  for(int T = 0; T < QWE; T++)
  {
    printf("Case #%d: ", T + 1);
    ReadData();
    Solve();
  }
  return 0;
}