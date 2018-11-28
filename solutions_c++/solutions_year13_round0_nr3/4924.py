#include <algorithm>
#include <cassert>
#include <cstdio>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#define ASSERT_ for (;;) {}
#define PII pair<int, int>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)
using namespace std;


int main() {
  int ntestcase;
  scanf("%d\n", &ntestcase);
  vector<int> data;
  REP(i,1001)
    data.push_back(0);
  data[1] = 1;
  data[4] = 1;
  data[9] = 1;
  data[121] = 1;
  data[484] = 1;
  for (int test_id = 1; test_id <= ntestcase; test_id++) {
    int res;
 
    int a,b;
    scanf("%d%d", &a, &b);
    res = accumulate(data.begin() + a, data.begin() + b + 1, 0);
     

    printf("Case #%d: %d\n", test_id, res);
  }

  return 0;
}
