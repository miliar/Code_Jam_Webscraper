#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;

int W, H, B;
struct Building {
  int x0, x1, y0, y1;
} buildings[1000];

long long distances[1002][1002];


typedef pair<double, unsigned> halfpijl; // gewicht en bestemming


long long dist[1002];
bool done[1002];
int dijkstra () {
  for(int i = 0; i < B + 2; ++i) {
    dist[i] = 1000000000000ll;
    done[i] = false;
  }

  dist[0] = 0;


  for(;;) {
    int choice = -1;
    long long m = 1000000000000ll;
    for(int i = 0; i < B+2; ++i) {
      //std::cout << i << " : " << done[i] << " " << dist[i]  << " " << m << "\n";
       if(!done[i] && dist[i] < m) { m = dist[i]; choice = i; }
    }
      // std::cout << "visit " << choice << " "  << dist[choice] << "\n";
       if(choice < 0)
         std::abort();
    done[choice] = true;
    if(choice == 1)
      return dist[1];
    for(int i = 0; i < B+2; ++i)
      dist[i] = std::min(dist[i], dist[choice] + distances[choice][i]);
  }

}
void doit (int casenum) {
  cin >> W >> H >> B;
  for(int i = 0; i < B; ++i)
    cin >>buildings[i].x0 >> buildings[i].y0 >> buildings[i].x1 >> buildings[i].y1;
  for(int i = 0; i < B; ++i)
    distances[0][i+2] = distances[i+2][0] = buildings[i].x0;
  for(int i = 0; i < B; ++i)
    distances[1][i+2] = distances[i+2][1] = W - buildings[i].x1 - 1;
  distances[0][1] = distances[1][0] = W;
  for(int i = 0; i < B; ++i) {
    for(int j = i + 1; j < B; ++j) {
        int x = std::max(buildings[i].x0 - buildings[j].x1 - 1, buildings[j].x0 - buildings[i].x1 - 1);
        int y = std::max(buildings[i].y0 - buildings[j].y1 - 1, buildings[j].y0 - buildings[i].y1 - 1);
        distances[i+2][j+2] = distances[j+2][i+2] = std::max(0, std::max(x, y));
    }
  }
 // std::cout << "step1\n";
  std::cout << "Case #" << casenum << ": " << dijkstra() << "\n";
}

int main () {
  int t;
  cin >> t;
  for(int i = 1; i <= t; ++i)
    doit(i);
  return 0;
}