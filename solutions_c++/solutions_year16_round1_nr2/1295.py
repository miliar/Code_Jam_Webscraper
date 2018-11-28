#include <iostream>
#include <cassert>
#include <vector>
#include <map>

using List = std::vector<int>;
using Lists = std::vector<List>;
using Hist = std::map<int, int>;

List getMissingList(const Lists& lists)
{
  Hist hist;

  for (const List& list : lists) {
    for (int height : list) {
      ++hist[height];
    }
  }

  List res;

  for (const auto& pair : hist) {
    if (pair.second % 2 == 0) {
      continue;
    }

    res.push_back(pair.first);
  }

  assert (!lists.empty());
  assert (res.size() == lists[0].size());
  return res;
}

int main()
{
  int cases = 0;
  std::cin >> cases;

  for (int i = 1; i <= cases; ++i) {
    int n = 0;
    std::cin >> n;

    Lists lists;
    for (int j = 0; j < 2 * n - 1; ++j) {
      List list;
      list.reserve(n);

      for (int k = 0; k < n; ++k) {
	int height = 0;
	std::cin >> height;

	list.push_back(height);
      }

      lists.push_back(list);
    }
    
    std::cout << "Case #" << i << ':';
    List missingList = getMissingList(lists);
    for (int height : missingList) {
      std::cout << ' ' << height;
    }
    std::cout << std::endl;
  }
  
  return 0;
}
