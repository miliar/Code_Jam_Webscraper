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
    printf("Case #%d: ", t+1);

    int n, k;

    scanf("%d%d", &n, &k);

    int sum[1001];
    int inmax[101];
    int intav[101];
    int inmin[101];

    int biggest = 0;
    int bignum = 0;

    for(int i = 0; i < n-k+1; ++i) {
      scanf("%d", &sum[i]);
    }


    for(int i = 0; i < k; ++i) {
      int num = 0;
      inmax[i] = 0;
      inmin[i] = 0;
      for(int j = i; j < n-k; j += k) {
        num += sum[j+1] - sum[j];
        inmax[i] = max(inmax[i], num);
        inmin[i] = min(inmin[i], num);
      }
    }

    int nyel = 0;

    for(int i = 0; i < k; ++i) {
      intav[i] = inmax[i] - inmin[i];
//      printf("%d ", intav[i]);
      if(intav[i] > biggest) {
        biggest = intav[i];
//        bignum = 1;
      } else if(biggest == intav[i]) {
        ++bignum;
      }
      sum[0] += inmin[i];
    }

    for(int i = 0; i < k; ++i) {
      nyel += biggest - intav[i];
    }

    int nagy = ((sum[0] % k) + k) % k;

//    printf("%d    ", nagy);

    if(nagy > nyel) {
      ++biggest;
    }

    printf("%d\n", biggest);


  }

  return 0;
}
