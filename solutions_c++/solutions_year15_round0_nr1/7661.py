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
  int tt,smax;
  char s[10001];
  scanf("%d", &tt);
  for (int i = 1; i <= tt; i++) {
    printf("Case #%d: ", i);
    fflush(stdout);
    scanf("%d",&smax);
    scanf("%s",s);
    int total = s[0] - '0';
    int frnds = 0;
    if(smax == 0)
      frnds = 0;
    else
      {
	for(int j=0; j<smax; j++){
	  if(j+1 > total)
	    {
	      frnds += j + 1 - total;
	      total += s[j+1] - '0' + j + 1 - total;
	    }
	  else
	    total += s[j+1] - '0';
	}
      }
    printf("%d\n", frnds);
    fflush(stdout);
  }
  return 0;
}
