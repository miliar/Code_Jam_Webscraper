#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long lglg;

int dist_array[1002*1002];

struct Building {
  int x0, y0, x1, y1;
};

Building buildings[1000];

int& dist(int x, int y) {
  return dist_array[x + 1002*y];
}

bool done[1002];
int way[1002];

int main()
{
  int T;
  scanf("%d", &T);

  int n1, n2, n3, n4;

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    int w, h, b;

    scanf("%d%d%d", &w, &h, &b);

    // 0 is left shore, 1 is right shore;

    for(int i = 0; i < b; ++i) {
      scanf("%d%d%d%d", &n1, &n2, &n3, &n4);

      buildings[i] = {n1, n2, n3, n4};
    }

    dist(0, 0) = 0;
    dist(1, 1) = 0;
    dist(0, 1) = w;
    dist(1, 0) = w;

    for(int i = 0; i < b; ++i) {
      dist(0, i+2) = buildings[i].x0;
      dist(i+2, 0) = buildings[i].x0;
      dist(1, i+2) = w - 1 - buildings[i].x1;
      dist(i+2, 1) = w - 1 - buildings[i].x1;
    }

//    printf("doing distances\n");

    for(int i = 0; i < b; ++i) {
      for(int j = 0; j < b; ++j) {
        int curdist = 0;
        if(buildings[i].x0 > buildings[j].x1) {
          curdist = std::max(buildings[i].x0 - buildings[j].x1 - 1, curdist);
        }
        if(buildings[j].x0 > buildings[i].x1) {
          curdist = std::max(buildings[j].x0 - buildings[i].x1 - 1, curdist);
        }
        if(buildings[i].y0 > buildings[j].y1) {
          curdist = std::max(buildings[i].y0 - buildings[j].y1 - 1, curdist);
        }
        if(buildings[j].y0 > buildings[i].y1) {
          curdist = std::max(buildings[j].y0 - buildings[i].y1 - 1, curdist);
        }

        dist(i+2, j+2) = curdist;
        dist(j+2, i+2) = curdist;
      }
    }

    for(int i = 0; i < 1002; ++i) {
      done[i] = false;
      way[i] = 2000;
    }

//    printf("doing walk\n");

    priority_queue<std::pair<int, int>, vector<pair<int, int>>, greater<std::pair<int, int>>> walk;

    walk.push(make_pair(0, 0));

    while(!walk.empty()) {
      auto p = walk.top();
      walk.pop();

      int d = p.first;
      int i = p.second;

      if(done[i]) continue;

      done[i] = true;


//      printf("walking %d, dist %d\n", i, d);

      if(i == 1) break;

      for(int j = 0; j < b+2; ++j) {
        if(d + dist(i, j) < way[j]) {
          walk.push(make_pair(d + dist(i, j), j));
          way[j] = d + dist(i, j);
        }
      }
    }

    printf("%d\n", way[1]);


  }

  return 0;
}
