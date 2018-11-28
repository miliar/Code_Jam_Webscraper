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

int sizes[10003];
bool used[10003];

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    int N, X;
    scanf("%d%d", &N, &X);

    for(int i = 0; i < N; ++i) {
      scanf("%d", sizes+i);
      used[i] = false;
    }

    sort(sizes, sizes+N);

    int i = 0, j = N-1;

    int result = N;

    while(i < j) {
      while(i < j && sizes[j] + sizes[i] > X) {
        --j;
      }

      if(i < j) {
        --result;
        ++i;
        --j;
      }
    }

    printf("%d\n", result);
  }

  return 0;
}
