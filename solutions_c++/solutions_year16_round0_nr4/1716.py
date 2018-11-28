#include <iostream>
#include <numeric>
#include <cassert>
#include <vector>
#include <iterator>

int main()
{
   int cases;
   std::cin >> cases;
   for (int test = 1; test <= cases; ++test) {
      int K, C, S;
      std::cin >> K >> C >> S;
      assert(K > 0 && K == S);
      std::vector<int> positions(K);
      std::iota(positions.begin(), positions.end(), 1);
      std::cout << "Case #" << test << ": ";
      std::copy(positions.begin(), positions.end(), std::ostream_iterator<int>(std::cout, " "));
      std::cout << '\n';
   }
}
