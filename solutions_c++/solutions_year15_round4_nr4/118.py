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

const lglg MOD = 1000000007ll;

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    int R, C;

    scanf("%d%d", &R, &C);

    lglg last_12[4][8], last_3[4][8];
    // index: volte3, volte4, volte6
    last_3[0][0] = 1;
    last_3[1][0] = 0;
    last_3[2][0] = 1;
    last_12[0][0] = 1;
    last_12[1][0] = 1;
    for(int f = 1; f < 8; ++f) {
      last_3[0][f] = 0;
      last_3[1][f] = 0;
      last_3[2][f] = 0;
      last_12[0][f] = 0;
      last_12[1][f] = 0;
      last_12[2][f] = 0;
    }
    last_12[2][0] = 0;
    if(C % 6 == 0) {
      last_12[2][5] = 1;
    }
    if(C % 3 == 0) {
      last_12[2][4] = 1;
    }
    int id = R;
    for(int i = 3; i <= R; ++i) {
      id = i % 4;

      for(int f = 0; f < 8; ++f) {
        last_3[id][f] = last_12[(id + 4 - 2) % 4][f];

        last_12[id][f] = last_3[(id + 4 - 1) % 4][f];
      }

      if(C % 3 == 0) {
        for(int f = 4; f < 8; ++f) {
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 2) % 4][f] * 3) % MOD;
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 2) % 4][f-4]) % MOD;
        }
      }

      if(C % 6 == 0) {
        for(int f = 5; f < 8; f += 2) {
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 2) % 4][f] * 6) % MOD;
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 2) % 4][f-1] * 3) % MOD;
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 2) % 4][f-5]) % MOD;
        }
      }

      if(C % 4 == 0) {
        for(int f = 2; f < 4; ++f) {
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 3) % 4][f] * 4) % MOD;
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 3) % 4][f-2]) % MOD;
        }
        for(int f = 6; f < 8; ++f) {
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 3) % 4][f] * 4) % MOD;
          last_12[id][f] = (last_12[id][f] + last_3[(id + 4 - 3) % 4][f-2]) % MOD;
        }
      }
    }
    lglg sum = 0;
    for(int f = 0; f < 8; ++f) {
      sum = (sum + last_3[id][f]) % MOD;
      sum = (sum + last_12[id][f]) % MOD;
    }
    int sum2 = int(sum);
    printf("%d\n", sum2);
  }

  return 0;
}
