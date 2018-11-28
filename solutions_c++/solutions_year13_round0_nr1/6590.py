#include <stdio.h>
#include <string.h>

using namespace std;

char grid[4][4];
int i, u, number_of_x, number_of_o, winners[2], t, c, number_of_dots;

int main()
{
  scanf("%d", &t);

  for (c = 0; c < t; c++)
  {
    memset(grid, 0, sizeof grid);
    memset(winners, 0, sizeof winners);
    number_of_dots = 0;

    for (i = 0; i < 4; i++)
    {
      for (u = 0; u < 4; u++)
      {
        scanf(" %c", &grid[i][u]);

        if (grid[i][u] == '.')
        {
          number_of_dots++;
        }
      }
    }

    /* Check columns */
    for (i = 0; i < 4; i++)
    {
      number_of_x = 0;
      number_of_o = 0;

      for (u = 0; u < 4; u++)
      {
        if (grid[u][i] == '.')
        {
          break;
        }

        if (grid[u][i] == 'T')
        {
          number_of_x++;
          number_of_o++;
        }

        if (grid[u][i] == 'X')
        {
          number_of_x++;
        }

        if (grid[u][i] == 'O')
        {
          number_of_o++;
        }
      }

      if (number_of_x == 4)
      {
        winners[0] = 1;
      }

      if (number_of_o == 4)
      {
        winners[1] = 1;
      }
    }

    /* Check rows */
    for (i = 0; i < 4; i++)
    {
      number_of_x = 0;
      number_of_o = 0;

      for (u = 0; u < 4; u++)
      {
        if (grid[i][u] == '.')
        {
          break;
        }

        if (grid[i][u] == 'T')
        {
          number_of_x++;
          number_of_o++;
        }

        if (grid[i][u] == 'X')
        {
          number_of_x++;
        }

        if (grid[i][u] == 'O')
        {
          number_of_o++;
        }
      }

      if (number_of_x == 4)
      {
        winners[0] = 1;
      }

      if (number_of_o == 4)
      {
        winners[1] = 1;
      }
    }

    /* Check left-to-right diagonal */
    number_of_x = 0;
    number_of_o = 0;

    for (i = 0; i < 4; i++)
    {
      if (grid[i][i] == '.')
      {
        break;
      }

      if (grid[i][i] == 'T')
      {
        number_of_x++;
        number_of_o++;
      }

      if (grid[i][i] == 'X')
      {
        number_of_x++;
      }

      if (grid[i][i] == 'O')
      {
        number_of_o++;
      }
    }

    if (number_of_x == 4)
    {
      winners[0] = 1;
    }

    if (number_of_o == 4)
    {
      winners[1] = 1;
    }

    /* Check right-to-left diagonal */
    number_of_x = 0;
    number_of_o = 0;

    for (i = 3; i >= 0; i--)
    {
      if (grid[3 - i][i] == '.')
      {
        break;
      }

      if (grid[3 - i][i] == 'T')
      {
        number_of_x++;
        number_of_o++;
      }

      if (grid[3 - i][i] == 'X')
      {
        number_of_x++;
      }

      if (grid[3 - i][i] == 'O')
      {
        number_of_o++;
      }
    }

    if (number_of_x == 4)
    {
      winners[0] = 1;
    }

    if (number_of_o == 4)
    {
      winners[1] = 1;
    }

    /* Print answer */
    if (winners[0] == 1)
    {
      printf("Case #%d: X won\n", c + 1);
    }
    else if (winners[1] == 1)
    {
      printf("Case #%d: O won\n", c + 1);
    }
    else
    {
      if (number_of_dots == 0)
      {
        printf("Case #%d: Draw\n", c + 1);
      }
      else
      {
        printf("Case #%d: Game has not completed\n", c + 1);
      }
    }

    scanf("\n");
  }

  return 0;
}
