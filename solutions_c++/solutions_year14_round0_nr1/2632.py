#include <algorithm>
#include <functional>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <vector>
using std::cin;
using std::cout;

std::vector<int> PossibleIds() {
  std::vector<int> possible;

  int answer;
  cin >> answer;
  --answer;

  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      int value;
      cin >> value;
      if (i == answer) {
        possible.push_back(value);
      }
    }
  }

  std::sort(possible.begin(), possible.end());
  return possible;
}

int main() {
  std::ios_base::sync_with_stdio(false);
//  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/1.txt", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/A-small-attempt1.in", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/A-small-attempt1.out", "wb", stdout);
  int T;
  cin >> T;

  for (int tc = 0; tc < T; ++tc) {

    std::vector<int> possible1 = PossibleIds();
    std::vector<int> possible2 = PossibleIds();

    std::vector<int> common;
    std::set_intersection(possible1.begin(),
                          possible1.end(),
                          possible2.begin(),
                          possible2.end(),
                          std::back_inserter(common));

    cout << "Case #" << tc + 1 << ": ";
    if (common.size() == 1) {
      cout << common.front();
    } else if (common.empty()) {
      cout << "Volunteer cheated!";
    } else {
      cout << "Bad magician!";
    }

    cout << '\n';
  }
  return 0;
}
