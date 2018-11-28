/* CodeJam solution up&down in C++ by domob.  */

/* Try all permutations.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdint.h>
#include <vector>

/* See if we have an up-down thing.  */
static bool
isUpDown (const std::vector<unsigned>& nums)
{
  bool maxFound = false;
  for (unsigned i = 0; i + 1 < nums.size (); ++i)
    {
      assert (nums[i] != nums[i + 1]);
      if (!maxFound && nums[i] < nums[i + 1])
        continue;

      if (maxFound && nums[i] < nums[i + 1])
        return false;

      if (maxFound && nums[i] > nums[i + 1])
        continue;

      assert (!maxFound && nums[i] > nums[i + 1]);
      maxFound = true;
    }

  return true;
}

/* Recursive search procedure.  */
static void
tryOut (std::vector<unsigned>& numbers, unsigned pos,
        unsigned cur, unsigned& best)
{
  assert (pos <= numbers.size ());
  if (pos == numbers.size ())
    {
      if (isUpDown (numbers) && cur < best)
        best = cur;
      return;
    }

  assert (pos < numbers.size ());
  for (unsigned target = pos; target < numbers.size (); ++target)
    {
      unsigned swaps = 0;
      for (unsigned i = target; i > pos; --i)
        {
          ++swaps;
          std::swap (numbers[i], numbers[i - 1]);
        }
      tryOut (numbers, pos + 1, cur + swaps, best);
      for (unsigned i = pos + 1; i <= target; ++i)
        std::swap (numbers[i], numbers[i - 1]);
    }
}

/* Solve a single case.  */
static void
solve_case ()
{
  unsigned n;
  scanf ("%u", &n);

  std::vector<unsigned> numbers(n);
  for (unsigned i = 0; i < n; ++i)
    scanf ("%u", &numbers[i]);

  unsigned res = 1000000000;
  tryOut (numbers, 0, 0, res);

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
