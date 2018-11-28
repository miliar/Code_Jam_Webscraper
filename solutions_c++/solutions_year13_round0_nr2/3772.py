/* CodeJam solution lawnmower in C++ by domob.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdint.h>

/* Solve a single case.  */
void
solve_case ()
{
  int n, m;
  int heights[100][100];
  scanf ("%d %d", &n, &m);

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      scanf ("%d", &heights[i][j]);

  /* Find maximal heights in each row and column.  This is the lowest possible
     setting for the mower when directing it along that row/column in order to
     not disturb the heighest desired place.  For each cell afterwards, the
     height must be not smaller than the value in its row or column.  */
  int colHeights[100];
  int rowHeights[100];
  std::fill (colHeights, colHeights + m, 0);
  std::fill (rowHeights, rowHeights + n, 0);
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      {
        colHeights[j] = std::max (colHeights[j], heights[i][j]);
        rowHeights[i] = std::max (rowHeights[i], heights[i][j]);
      }

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      {
        if (heights[i][j] < std::min (colHeights[j], rowHeights[i]))
          {
            printf ("NO");
            return;
          }
      }

  printf ("YES");
}

/* Main routine, handling the different cases.  */
int
main ()
{
  int n;

  scanf ("%d\n", &n);
  for (int i = 1; i <= n; ++i)
    {
      printf ("Case #%d: ", i);
      solve_case ();
      printf ("\n");
    }

  return EXIT_SUCCESS;
}
