#include <iostream>
#include <stdio.h>
using namespace std;

inline int DefWinner(int sum)
{
  if (sum == (3 * 'X' + 'T') || sum == 4 * 'X')
    return 'X';
  if (sum == (3 * 'O' + 'T') || sum == 4 * 'O')
    return 'O';
  return 0;
}

int main(void)
{
  FILE *f = fopen("A-large.in", "r");
  
  if (!f)
    return 1;
  int n = 0;
  fscanf(f, "%i", &n);
  char str[255];
  fgets(str, 254, f);
  char **fields = new char*[4 * n];
  for (int i = 0; i < n; i++)
  {
    for (int j = 4 * i; j < 4 * i + 4; j++)
    {
      fields[j] = new char[6];
      fgets(fields[j], 6, f);
    }
    fgets(str, 254, f);
  }
  fclose(f);

  int sum;
  char answer;
  int emptyCell = 0;
  f = fopen("output.txt", "w");
  for (int i = 0; i < n; i++)
  {
    if (i)
      fprintf(f, "\n");
    emptyCell = 0;

    for (int k = 0; k < 4; k++)
    {
      sum = 0;
      for (int j = 0; j < 4; j++)
      {
        if (fields[i * 4 + k][j] == '.')
          emptyCell = 1;
        sum += fields[i * 4 + k][j];
      }
      if (answer = DefWinner(sum))
        goto WriteAnswer;
    }

    for (int k = 0; k < 4; k++)
    {
      sum = 0;
      for (int j = 0; j < 4; j++)
        sum += fields[i * 4 + j][k];
      if (answer = DefWinner(sum))
        goto WriteAnswer;
    }

    sum = 0;
    for (int j = 0; j < 4; j++)
      sum += fields[i * 4 + j][j];
    if (answer = DefWinner(sum))
      goto WriteAnswer;

    sum = 0;
    for (int j = 0; j < 4; j++)
      sum += fields[i * 4 + j][3 - j];
    if (answer = DefWinner(sum))
      goto WriteAnswer;
    
    if (emptyCell)
      fprintf(f, "Case #%i: Game has not completed", i + 1);
    else
      fprintf(f, "Case #%i: Draw", i + 1);
    continue;

WriteAnswer:
    fprintf(f, "Case #%i: %c won", i + 1, answer);
  }
  fclose(f);
  return 0;
}