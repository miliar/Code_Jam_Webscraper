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
int OFF = 250;
struct Node {
  int d, n, w, e, s, delta_d, delta_p, delta_s, done;
};
int main()
{
  int tests;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    int N;
    std::cin >> N;
    std::vector<Node> v(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> v[i].d >> v[i].n >> v[i].w >> v[i].e >> v[i].s
               >> v[i].delta_d >> v[i].delta_p >> v[i].delta_s;
    }
    int ans = 0;
    std::vector<int> wall(500);
    for(int i = 0; i < 676070; ++i) {
      std::vector<int> z(wall.size());
      bool update = false;
      for(int j = 0; j < N; ++j) {
        if(v[j].d != i || v[j].n <= v[j].done) continue;
        //std::cout << "DAY " << i << " attack by tribe " << j << std::endl;
        int dd = v[j].done*v[j].delta_p;
        int w = dd + v[j].w;
        int e = dd + v[j].e;
        int s = v[j].done*v[j].delta_s + v[j].s;
        bool success = false;
        for(int k = w; k < e; ++k) {
          if(wall[k+OFF] < s) {
            success = true;
            update = true;
            z[k+OFF] = std::max(z[k+OFF], s);
          }
        }
        if(success) {
          //std::cout << "SUCCESS" << std::endl;
          ++ans;
        }
        v[j].d += v[j].delta_d;
        ++v[j].done;
      }
      if(update) {
        for(int j = 0; j < (int)wall.size(); ++j) {
          wall[j] = std::max(wall[j], z[j]);
        }
      }
    }
    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}

