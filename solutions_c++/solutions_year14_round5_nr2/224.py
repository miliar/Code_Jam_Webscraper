/* Opgave: B */
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
#include <unordered_map>
#include <unordered_set>
#include <tuple>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;

int N, P, Q;


int H[100];
int G[100];

std::map<std::tuple<int, int, bool>, int> mem;
int getGold(int m, int shots, bool shoot) {
  if(m == N)
    return 0;
  if(mem.find(std::tuple<int, int, bool>{m, shots, shoot}) != mem.end())
    return mem.find(std::tuple<int, int, bool>{m, shots, shoot}) ->second;
  int towerShots = (H[m] + Q - 1) / Q;
  int ownShots = shoot ? towerShots  : (towerShots - 1);
  int gold = getGold(m + 1, shots + ownShots, true);
  if((ownShots + shots) * P >= H[m] - Q * (towerShots - 1)) {
    int killShots = (H[m] - Q * (towerShots - 1) + P - 1) / P;
    int g2 = getGold(m + 1, shots + ownShots - killShots , false) + G[m];
    gold = max(gold, g2);
  }
  mem[std::tuple<int, int, bool>{m, shots, shoot}] = gold;
  //std::cout << " " << m << " " << shots << " " << shoot << " " << gold << "\n";
  return gold;
}
void doit (int casenum) {
  cin >> P >> Q >> N;
  mem.clear();
  for(int i = 0; i < N; ++i)
    cin >> H[i] >> G[i];
  std::cout << "Case #" << casenum << ": " << getGold(0, 0, true) << "\n";
}

int main () {
  int T;
  cin >> T;
  for(int i = 1; i <= T; ++i)
    doit(i);
  return 0;
}
/* Opgave: B */
