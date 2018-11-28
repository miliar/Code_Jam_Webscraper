#include <iostream>
#include <cassert>

int main()
{
  int cases = 0;
  std::cin >> cases;

  for (int i = 1; i <= cases; ++i) {
    int k = 0;
    int c = 0;
    int s = 0;

    std::cin >> k >> c >> s;

    assert (k == s);

    // The first tile in the original sequence is either L or G.
    // If it's L, the first K tiles of the artwork always contain the original sequence.
    // If it's G, they always contain all Gs. Either way, they provide sufficient information
    // to decide whether the original has any Gs, which is true iff the entire artwork has any Gs.
    std::cout << "Case #" << i << ':';
    for (int j = 1; j <= k; ++j) {
      std::cout << ' ' << j;
    }
    std::cout << std::endl;
  }
  
  return 0;
}
