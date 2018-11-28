#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
#include <iomanip>
#define INF 2147483647
using namespace std;

int main(int argc, const char * argv[]) {

  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  int cases, currCase = 0;
  double totalTime, stageTime, c, f, x, r;
  cin >> cases;
  while(currCase++ < cases) {
    cin >> c >> f >> x;
    r = 2.0;
    totalTime = 0.0;
    while(1) {
      if ( x/r <= (c/r + x/(r+f))) {
        totalTime += x/r;
        break;
      } else {
        totalTime += c/r;
        r += f;
      }
    }
    cout << "Case #" << currCase << ": " << fixed << std::setprecision(7) << totalTime << endl;
  }
  return 0;
}
