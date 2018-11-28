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

int invit(int sl, char *as)
{
	int i = 0 ;
	int ttl = 0;
	int inv = 0;
	int row;
    ttl = as[i]-'0';
	for (i=1;i<=sl;i++){
		row = as[i]-'0';
		if ( ttl  < i ) {
			inv += (i-ttl);
			ttl = i+row;
		} else {
			ttl += row ;
		}
	}
	return inv;
}


int main() {
	int tt; int sl;int ret;
	char str[1002];
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
	scanf("%d", &sl);
	scanf("%s", &str);
	ret = invit(sl, str);
	 printf("%d\n", ret);
  }
  return 0;
}
