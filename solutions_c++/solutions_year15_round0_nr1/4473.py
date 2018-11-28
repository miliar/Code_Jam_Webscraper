
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
  size_t T; 
  std::cin >> T;

  for( size_t t = 1; t <= T; ++t )
  {
    size_t n;
    std::string s;
    {
      std::cin >> n;
      std::cin >> s;
      std::cerr << "DEBUG #" << t << ": " << n << " " << s << std::endl;
    }

    // Find the missing sum
    size_t m = 0;
    {
      // Actual sum
      size_t a = 0;

      // Loop through the sequence
      for( size_t i = 0; i <= n; ++i )
      {
        // Get the number of friends with this shyness level
        a += (s[i] - '0');

        // If there is not enough
        if( a < (i + 1) )
        {
          // Find the number of missing friends
          size_t d = (i - a + 1);

          // Increament the actual sum and number of missing friends
          a += d;
          m += d;
        }
      }
    }

    std::cout << "Case #" << t << ": " << m << std::endl;
  }

  return 0;
}

//--------------------------------------------------------------------------
// End-of-file
//--------------------------------------------------------------------------

