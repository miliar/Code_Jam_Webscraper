/* CodeJam solution packing in C++ by domob.  */

/* Simply a greedy algorithm:  Pack a large file on the disk, and see if any
   of the smaller ones fits, too.  Use the largest file that also fits.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdint.h>
#include <set>


/* Solve a single case.  */
void
solve_case ()
{
  unsigned n, cap;
  scanf ("%u %u\n", &n, &cap);

  std::multiset<unsigned, std::greater<unsigned>> files;
  for (unsigned i = 0; i < n; ++i)
    {
      unsigned cur;
      scanf ("%u", &cur);
      files.insert (cur);
    }
  assert (files.size () == n);

  unsigned res = 0;
  while (!files.empty ())
    {
      ++res;

      const auto end = files.begin ();
      const unsigned last = *end;
      files.erase (end);

      if (files.empty ())
        break;

      const unsigned remaining = cap - last;
      const auto next = files.lower_bound (remaining);
      if (next != files.end ())
        files.erase (next);
    }
  printf ("%u", res);
}

/* Main routine, handling the different cases.  */
int
main ()
{
  unsigned n;

  //std::cin >> n;
  scanf ("%u\n", &n);
  for (unsigned i = 1; i <= n; ++i)
    {
      //std::cout << "Case #" << i << ": ";
      printf ("Case #%u: ", i);

      solve_case ();

      //std::cout << std::endl;
      printf ("\n");
    }

  return EXIT_SUCCESS;
}
