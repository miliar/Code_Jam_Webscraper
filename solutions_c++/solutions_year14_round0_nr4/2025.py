/* CodeJam solution War in C++11 by domob.  */

#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <deque>
#include <stdint.h>

typedef double realT;
typedef std::deque<realT> realArr;

/* Simulate ordinary war.  Return Naomi's points.  The vectors are copied
   so that we can mess around with them.  */
unsigned
simulateWar (realArr naomi, realArr ken)
{
  unsigned res = 0;
  while (!naomi.empty ())
    {
      if (naomi.back () > ken.back ())
        {
          ++res;
          naomi.pop_back ();
          ken.pop_front ();
        }
      else
        {
          const auto iter = std::upper_bound (ken.begin (), ken.end (),
                                              naomi.back ());
          assert (*iter > naomi.back ());
          ken.erase (iter);
          naomi.pop_back ();
        }
    }

  return res;
}

/* Simulate deceitful war, as above.  */
unsigned
simulateDWar (realArr naomi, realArr ken)
{
  unsigned res = 0;
  while (!naomi.empty ())
    {
      if (naomi.back () > ken.back ())
        {
          ++res;
          naomi.pop_back ();
          ken.pop_back ();
        }
      else
        {
          naomi.pop_front ();
          ken.pop_back ();
        }
    }

  return res;
}

/* Solve a single case.  */
void
solve_case ()
{
  unsigned n;
  scanf ("%u\n", &n);

  realArr naomi(n);
  realArr ken(n);
  for (unsigned i = 0; i < n; ++i)
    scanf ("%lf", &naomi[i]);
  for (unsigned i = 0; i < n; ++i)
    scanf ("%lf", &ken[i]);

  std::sort (naomi.begin (), naomi.end ());
  std::sort (ken.begin (), ken.end ());

  /* For Ken, the best that can be achieved is to score a point with
     each block.  Thus whenever he can, he should do it as soon as possible.
     That is, when there is a block larger than Naomi's, use the smallest
     of those.  Otherwise, use the smallest at all, to not waste anything.

     For Naomi, it doesn't really matter, in which order she plays the blocks
     (?) in "War".  For "Deceitful War", she should play her smallest blocks
     first but tell Ken just a little lower than his own largest block.  */

  const unsigned war = simulateWar (naomi, ken);
  const unsigned deceitful = simulateDWar (naomi, ken);

  printf ("%u %u", deceitful, war);
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
