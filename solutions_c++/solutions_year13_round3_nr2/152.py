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
  std::string path;
  int step, x, y;
  Node(const std::string& path,
       int step, int x, int y):path(path), step(step), x(x), y(y) {}
};
int MAX = 150000;
static const int dx[] = { 1, 0, -1, 0 };
static const int dy[] = { 0, 1,  0,-1 };
char dir(int n)
{
  const char x[] = "ENWS";
  return x[n];
}
int main()
{
  int tests;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    int X, Y;
    std::cin >> X >> Y;
    std::queue<Node> q;
    q.push(Node("", 1, 0, 0));
    std::map<std::pair<int, int>, int> used;
    used[std::make_pair(0, 0)] = 1;
    std::string ans;
    while(!q.empty()) {
      Node node = q.front();
      q.pop();
      if(node.x == X && node.y == Y) {
        ans = node.path;
        break;
      }
      for(int i = 0; i < 4; ++i) {
        int nx = node.x + node.step*dx[i], ny = node.y + node.step*dy[i];
        std::pair<int, int> key(nx, ny);
        if(used.count(key) == 0 && abs(nx) <= MAX && abs(ny) <= MAX) {
          used[key] = 1;
          q.push(Node(node.path+dir(i), node.step+1, nx, ny));
        }
      }
    }
    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}

