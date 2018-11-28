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

int main()
{
  int T;

  string best[13][3];

  best[0][0] = "P";
  best[0][1] = "R";
  best[0][2] = "S";

  for(int i = 1; i <= 12; ++i) {
    // P
    if(best[i-1][0] < best[i-1][1]) {
      best[i][0] = best[i-1][0] + best[i-1][1];
    } else {
      best[i][0] = best[i-1][1] + best[i-1][0];
    }
    // R
    if(best[i-1][1] < best[i-1][2]) {
      best[i][1] = best[i-1][1] + best[i-1][2];
    } else {
      best[i][1] = best[i-1][2] + best[i-1][1];
    }
    // P
    if(best[i-1][2] < best[i-1][0]) {
      best[i][2] = best[i-1][2] + best[i-1][0];
    } else {
      best[i][2] = best[i-1][0] + best[i-1][2];
    }

//    printf("%s %s %s\n", best[i][0].c_str(), best[i][1].c_str(), best[i][2].c_str());
  }

  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    int n, r, p, s;

    scanf("%d%d%d%d", &n, &r, &p, &s);

    vector<string> goods;


    if(count(best[n][0].begin(), best[n][0].end(), 'P') == p &&
       count(best[n][0].begin(), best[n][0].end(), 'R') == r &&
       count(best[n][0].begin(), best[n][0].end(), 'S') == s) {
      goods.push_back(best[n][0]);
    }
    if(count(best[n][1].begin(), best[n][1].end(), 'P') == p &&
       count(best[n][1].begin(), best[n][1].end(), 'R') == r &&
       count(best[n][1].begin(), best[n][1].end(), 'S') == s) {
      goods.push_back(best[n][1]);
    }
    if(count(best[n][2].begin(), best[n][2].end(), 'P') == p &&
       count(best[n][2].begin(), best[n][2].end(), 'R') == r &&
       count(best[n][2].begin(), best[n][2].end(), 'S') == s) {
      goods.push_back(best[n][2]);
    }

    if(goods.empty()) {
      printf("IMPOSSIBLE\n");
    }else {
      sort(goods.begin(), goods.end());
      printf("%s\n", goods[0].c_str());
    }

  }

  return 0;
}
