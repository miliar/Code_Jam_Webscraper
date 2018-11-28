#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cfloat>
#include <climits>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <utility>
#include <sys/time.h>

#define INF 1000000007
#define EPS (1e-8)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define mp make_pair
#define FOR(i,k) for(i=0;i<k;i++)
#define RFOR(i,k) for(i=k-1;i>=0;i--)
const long double PI = 3.1415926535897932384626433832795;
typedef long long LL;

using namespace std;

bool AllDigitsSeen(vector<bool>* seen) {
  for (int i = 0; i < 10; i++) {
    if ((*seen)[i] == false)
      return false;
  }
  return true;
}

void UpdateSeen(vector<bool>* seen, LL curr) {
  LL tmp = curr;
  while (tmp > 0) {
    LL dig = tmp%10;
    tmp = tmp/10;
    (*seen)[dig] = true;
  }
}

LL GetAns(vector<bool>* seen, LL curr) {
  if (curr == 0)
    return -1;    

  LL tmp = curr;
  while (true) {
    UpdateSeen(seen, tmp);

    if (AllDigitsSeen(seen))
      return tmp;

    tmp = tmp + curr;
  }
}

main()
{
  int tests;
  scanf ("%d", &tests);

  for (int tc = 1; tc <= tests; tc++) {
    int num;
    scanf("%d", &num);

    LL lnum = num;
    vector<bool> seen(10, false);
    LL ans = GetAns(&seen, lnum);

    printf("Case #%d: ",tc);
    if (ans == -1) {
      printf("INSOMNIA\n");
    }
    else {
      printf("%lld\n", ans);
    }
  }
}


