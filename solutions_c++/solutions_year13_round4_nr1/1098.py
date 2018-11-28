#include <limits.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
#include <map>
#include <utility>
static const int INF = std::numeric_limits<int>::max();
struct Node {
  int o, e, num;
  Node():o(0),e(0),num(0) {}
  Node(int o, int e, int num) : o(o), e(e), num(num) {}
  bool operator<(const Node& rhs) const
  {
    return o < rhs.o || (o == rhs.o && e < rhs.e);
  }
};
int sum(const std::vector<Node>& v, int N)
{
  int res = 0;
  for(auto& a : v) {
    int n = a.e - a.o;
    res += (N*(N+1)/2-(N-n)*(N-n-1)/2)*a.num;
  }
  return res;
}
bool intersect(const Node& a, const Node& b)
{
  return std::max(a.o, b.o) <= std::min(a.e, b.e) &&
    (!(a.o < b.o && b.e < a.e) &&
     !(b.o < a.o && a.e < b.e) &&
     a.o != b.o && a.e != b.e);
}
int main()
{
  int tests;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    int N, M;
    std::cin >> N >> M;
    std::vector<Node> v(M);
    for(int i = 0; i < M; ++i) {
      std::cin >> v[i].o >> v[i].e >> v[i].num;
    }
    int sum1 = sum(v, N);
    std::vector<Node> comp;
    std::sort(v.begin(), v.end());
    while(!v.empty()) {
      std::vector<Node> v2;
      for(int i = 1; i < (int)v.size(); ++i) {
        if(v[0].o < v[i].o && v[0].e < v[i].e && v[0].e >= v[i].o) {
          //std::cout << "overlap" << std::endl;
          int cnum = std::min(v[0].num, v[i].num);
          if(v[0].num > cnum) {
            v2.push_back(Node(v[0].o, v[0].e, v[0].num-cnum));
          } else if(v[i].num > cnum) {
            v2.push_back(Node(v[i].o, v[i].e, v[i].num-cnum));
          }
          v2.push_back(Node(v[i].o, v[0].e, cnum));
          v[0].e = v[i].e;
          v[0].num = cnum;
        } else {
          v2.push_back(v[i]);
        }
      }
      comp.push_back(v[0]);
      std::sort(v2.begin(), v2.end());
      v.swap(v2);
    }
    // for(auto& a : comp) {
    //   std::cout << a.o << " " << a.e << " " << a.num << std::endl;
    // }
    int res = sum1 - sum(comp, N);
    std::cout << "Case #" << test << ": " << res << std::endl;
  }
}

