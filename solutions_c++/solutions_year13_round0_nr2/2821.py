#include <stdlib.h>
#include <stdio.h>

const char *check_field(int field[100][100], int N, int M)
{
    int i, j, k, direction;
    int template_field[100][100];
    if (N == 1 || M == 1)
        return ("YES");

    i = 0;
    while (i < N)
    {
        j = 0;
        while (j < M)
        {
	    template_field[i][j] = 2;
            ++j;
        }
        ++i;
    }

    i = 0;
    while (i < N)
    {
      direction = 1;
      j = 0;
      while (j < M)
      {
	if (field[i][j] != field[i][0])
	{
	  direction = 0;
	  break;
	}
	++j;
      }
      if (direction)
      {
	j = 0;
	while (j < M)
	{
	  template_field[i][j] = field[i][0];
	  ++j;
	}
      }
      ++i;
    }
    
    j = 0;
    while (j < M)
    {
      direction = 1;
      i = 0;
      while (i < N)
      {
	if (field[i][j] != field[0][j])
	{
	  direction = 0;
	  break;
	}
	++i;
      }
      if (direction)
      {
	i = 0;
	while (i < N)
	{
	  template_field[i][j] = field[0][j];
	  ++i;
	}
      }
      ++j;
    }    
    
    i = 0;
    while (i < N)
    {
        j = 0;
        while (j < M)
        {
	    if (template_field[i][j] != field[i][j])
	      return ("NO");
            ++j;
        }
        ++i;
    }
    
    return ("YES");
}

int main(void)
{
    int iT, T, N, M, i, j;
    int field[100][100];
    scanf("%d", &T);
    iT = 0;
    while (iT < T)
    {
        scanf("%d%d", &N, &M);
        i = 0;
        while (i < N)
        {
            j = 0;
            while (j < M)
            {
                scanf("%d", &field[i][j]);
                ++j;
            }
            ++i;
        }
        printf("Case #%d: %s\n", iT + 1, check_field(field, N, M));
        ++iT;
    }
    return (EXIT_SUCCESS);
}
