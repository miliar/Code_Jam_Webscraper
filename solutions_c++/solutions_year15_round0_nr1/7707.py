#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {

  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tc, max, current;

  int r;

  scanf("%d", &tc);
  for (int i=1;i<=tc;i++) {

    printf("Case #%d: ", i);

    scanf("%d", &max);
    int s[max+1];
    current = 0;
    r = 0;

    for (int j=0; j<=max; j++) {
      scanf("%1d", &s[j]);
      while(s[j] > 0 && j > current)
      {
        r++;
        current++;
      }
      current+=s[j];
    }

    cout << r << endl;
  }

  return 0;

}