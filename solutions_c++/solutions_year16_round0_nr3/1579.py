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
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d:\n", t+1);

    int n, j;

    scanf("%d%d", &n, &j);

    for(int i = 0; i < j; ++i) {
      printf("11");
      int k = i;
      for(int i = 0; i < (n - 4) / 2; ++i) {
        if(k % 2) {
          printf("11");
        } else {
          printf("00");
        }
        k /= 2;
      }
      printf("11 3 4 5 6 7 8 9 10 11\n");
    }


  }

  return 0;
}
