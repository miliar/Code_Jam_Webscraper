#include <cstdio>

void load(int* pos)
{
  int row = 0;
  scanf("%d", &row);
  for (int r = 1; r <= 4; ++r)
  {
    for (int c = 1; c <= 4; ++c)
    {
      int n = 0;
      scanf("%d", &n);
      if (r == row) pos[c - 1] = n;
    }
  }
}

int main()
{
  int pos1[4];
  int pos2[4];
  int cases = 0;
  scanf("%d", &cases);
  for (int cc = 1; cc <= cases; ++cc)
  {
    load(pos1);
    load(pos2);
    
    int sol = 0;
    int solc = 0;
    for (int p1 = 0; p1 < 4; ++p1)
    {
      for (int p2 = 0; p2 < 4; ++p2)
      {
        if (pos1[p1] == pos2[p2])
        {
          ++solc;
          sol = pos1[p1];
        }
      }
    }

    printf("Case #%d: ", cc);
    if (solc == 0)
    {
      printf("Volunteer cheated!\n");
    }
    else if (solc == 1)
    {
      printf("%d\n", sol);
    }
    else
    {
      printf("Bad magician!\n");
    }
  }
}

