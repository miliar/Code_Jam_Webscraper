#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int compare(int x[5], int y[5])
{
  int match = 0;
  bool match_already = false;
  for (int i = 0; i < 4; i++)
  for (int j = 0; j < 4; j++)
  {
    if (x[i] == y[j])
    {
      if (!match_already)
      {
        match = x[i];
        match_already = true;
      }
      else
        return -1;
    }
  }
  return match;
}
int main()
{
  int testcases;
  scanf("%d", &testcases);
  for (int testcase = 1; testcase <= testcases;testcase++)
  {
    printf("Case #%d:", testcase);
    int x[5];
    int y[5];
    int cnt = 1;
    int row, col;
    int tmp;
    scanf("%d", &row);
    for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
    {
      if (i + 1 == row)
      {
        scanf("%d", &x[j]);
      }
      else
        scanf("%d", &tmp);
    }
    scanf("%d", &col);
    for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
    {
      if (i + 1 == col)
      {
        scanf("%d", &y[j]);
      }
      else
        scanf("%d", &tmp);
    }
    int z = compare(x, y);
    if (z == 0)
    {
      printf(" Volunteer cheated!\n");
    }
    else if (z == -1)
    {
      printf(" Bad magician!\n");
    }
    else
    {
      printf(" %d\n", z);
    }
  }
  return 0;
}