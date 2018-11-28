#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <climits>
#include <fcntl.h>
#include <unistd.h>

using namespace std;

template <class T>
void splitstr(const string &s, vector<T> &out) {
  istringstream in(s);
  out.clear();
  copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

std::string solve(int x, std::string l) {
  // 0 1 2 3  4  5  6  7
  // 1 i j k -1 -i -j -k
  int table[8][8] = {{0, 1, 2, 3, 4, 5, 6, 7},
                     {1, 4, 3, 6, 5, 0, 7, 2},
                     {2, 7, 4, 1, 6, 3, 0, 5},
                     {3, 2, 5, 4, 7, 6, 1, 0},
                     {4, 5, 6, 7, 0, 1, 2, 3},
                     {5, 0, 7, 2, 1, 4, 3, 6},
                     {6, 3, 0, 5, 2, 7, 4, 1},
                     {7, 6, 1, 0, 3, 2, 5, 4}};

  std::vector<int> t(l.size());
  for (int i = 0; i < l.size(); ++i) {
    t[i] = l[i] - 104;
  }

  std::vector<int> t2(l.size() * x);
  auto dst_it = t2.begin();
  for (int i = 0; i < x; ++i) {
    dst_it = copy(t.begin(), t.end(), dst_it);
  }
  auto m = t2;

  std::vector<int> fwd(m.size());
  int f = 0;
  for (int i = 0; i < m.size(); ++i) {
    f = table[f][m[i]];
    fwd[i] = f;
  }

  std::vector<int> bck(m.size());
  int b = 0;
  for (int i = m.size() - 1; i >= 0; --i) {
    b = table[m[i]][b];
    bck[i] = b;
  }

  for (int f = 1; f < m.size() - 1; ++f) {
    int ps = fwd[f - 1];
    bool first_subset = ps == 1;
    if (!first_subset) continue;

    for (int s = f + 1; s < m.size(); ++s) {
      int st0 = fwd[f - 1];
      int ls0 = fwd[s - 1];
      if (table[st0][2] != ls0) continue;

      if (bck[s] != 3) continue;
      return "YES";
    }
  }
  return "NO";
}

int main() {
  vector<string> src;
  for (string line; getline(std::cin, line);) {
    src.push_back(line);
  }

  auto it = src.begin();
  ++it;

  int idx = 1;
  for (; it != src.end();) {
    std::vector<int> a;
    splitstr(*it++, a);
    auto x = a[1];
    auto l = *it++;
    std::cout << "Case #" << idx++ << ": " << solve(x, l) << std::endl;
  }

  return 0;
}
