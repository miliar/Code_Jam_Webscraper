
//--------------------------------------------------------------------------
// Require-header-file(s)
//--------------------------------------------------------------------------

// Standard-library
#include <algorithm>
#include <deque>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>

// Common using type
typedef bool                    bool_type;
typedef size_t                  size_type;
typedef long long               item_type;
typedef std::deque< item_type > ideq_type;

int main( int     argc, 
          char ** argv )
{
  char winner[][8] =
  {
    "GABRIEL",
    "RICHARD"
  };

  size_t T; 
  std::cin >> T;

  // Foreach test case
  for( size_t t = 1; t <= T; ++t )
  {
    size_t x, r, c;
    std::cin >> x >> r >> c;

    bool is_richard_winner =
      (x != 1) &&               // With 1-minos, GABRIEL always win
      (false
        || (0 != ((r * c) % x)) // Board size is not fit with x-minos
        || ((x > r) && (x > c)) // Use too long 1D x-minos
        || (x >= (2 * r + 1))    // Use too big 2D x-minos
        || (x >= (2 * c + 1))    // Use too big 2D x-minos
        || (x >= 7)             // Use x-minos with hole
        || ((x >= 4) &&
            (x >= ((r * c + 1)/2))) // Use too separate 2D x-minos
      );

    std::cout
      << "Case #" << t << ": "
      << winner[is_richard_winner] << std::endl;
  }

  return 0;
}

//--------------------------------------------------------------------------
// End-of-file
//--------------------------------------------------------------------------

