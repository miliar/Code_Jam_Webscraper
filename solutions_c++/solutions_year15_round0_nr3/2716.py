/* CodeJam solution Dijkstra in C++ by domob.  */

/* Solution for small:  Just expand the string and try out all possible
   splitting positions.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdint.h>
#include <sstream>

struct Quaternion
{
  char base;
  bool neg;
};

/* Multiply two single quaternions.  */
static Quaternion
operator* (const Quaternion& a, const Quaternion& b)
{
  Quaternion res;
  bool negate = false;

  if (a.base == '1')
    res.base = b.base;
  else if (b.base == '1')
    res.base = a.base;
  else if (a.base == b.base)
    {
      negate = true;
      res.base = '1';
    }
  else
    {
      switch (a.base)
        {
        case 'i':
          switch (b.base)
            {
            case 'j':
              res.base = 'k';
              break;
            case 'k':
              res.base = 'j';
              negate = true;
              break;
            default:
              assert (false);
            }
          break;

        case 'j':
          switch (b.base)
            {
            case 'i':
              res.base = 'k';
              negate = true;
              break;
            case 'k':
              res.base = 'i';
              break;
            default:
              assert (false);
            }
          break;

        case 'k':
          switch (b.base)
            {
            case 'i':
              res.base = 'j';
              break;
            case 'j':
              res.base = 'i';
              negate = true;
              break;
            default:
              assert (false);
            }
          break;

        default:
          assert (false);
        }
    }

  res.neg = (a.neg && !b.neg) || (!a.neg && b.neg);
  if (negate)
    res.neg = !res.neg;
  return res;
}

/* Try adjusting the second split boundary and see if we can get a "jk".
   Both quaternions are updated by multiplying from right and left
   with the changed value.  */
static bool
splitRemainder (const std::string& str, Quaternion& middle, Quaternion& last,
                unsigned pos)
{
  while (true)
    {
      if (middle.base == 'j' && !middle.neg
          && last.base == 'k' && !last.neg)
        return true;

      if (pos == str.size ())
        return false;

      Quaternion cur{str[pos], false};
      middle = middle * cur;
      cur.neg = true;
      last = cur * last;

      ++pos;
    }
}

/* Solve a single case.  */
static void
solve_case ()
{
  unsigned l, x;
  std::cin >> l >> x;
  std::string baseStr;
  std::cin >> baseStr;

  std::ostringstream strOut;
  for (unsigned i = 0; i < x; ++i)
    strOut << baseStr;
  const std::string str = strOut.str ();

  Quaternion first{'1', false};
  for (unsigned i = 0; i < str.size () - 1; ++i)
    {
      const Quaternion cur{str[i], false};
      first = first * cur;

      if (first.base == 'i' && !first.neg)
        {
          Quaternion middle{str[i + 1], false};
          Quaternion last{'1', false};
          for (unsigned j = i + 2; j < str.size (); ++j)
            {
              const Quaternion cur{str[j], false};
              last = last * cur;
            }

          if (splitRemainder (str, middle, last, i + 2))
            {
              std::cout << "YES";
              return;
            }
        }
    }

  std::cout << "NO";
}

/* Main routine, handling the different cases.  */
int
main ()
{
  Quaternion i{'i', false};
  Quaternion j{'j', false};
  Quaternion res;
  res = i * j;
  assert (res.base == 'k' && !res.neg);
  res = j * i;
  assert (res.base == 'k' && res.neg);

  unsigned n;
  std::cin >> n;
  for (unsigned i = 1; i <= n; ++i)
    {
      std::cout << "Case #" << i << ": ";
      solve_case ();
      std::cout << std::endl;
    }

  return EXIT_SUCCESS;
}
