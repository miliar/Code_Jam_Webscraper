#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>

typedef long long int lld;

int main()
{
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cin.exceptions(std::ios_base::failbit | std::ios_base::badbit);
  int testcases = 0; std::cin >> testcases;

  for (int case_nr=1; case_nr<=testcases; ++case_nr) {
    std::cout << "Case #" << case_nr << ": ";    

    int x, y; std::cin >> x >> y;
    if (y > 0) while (y--) std::cout << "SN";
    else       while (y++) std::cout << "NS";

    if (x > 0) while (x--) std::cout << "WE";
    else       while (x++) std::cout << "EW";
    
    std::cout << '\n';
  }
}

/*
 * Local variables:
 * mode:c++
 * compile-command:"rm -f fast-pogo && g++ -Ofast -flto -march=native -std=c++11 pogo.cc -o fast-pogo >/dev/null &; g++ -g -ggdb3 -O0 -D_GLIBCXX_DEBUG -Wall -Wextra -pedantic -Wno-long-long -std=c++11 pogo.cc -o pogo && for f in *.in; do echo \"--- $f -------------\"; ./pogo <$f; done"
 * end:
 */
