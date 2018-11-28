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

int main()
{
	freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  int case_index =1;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
  	int smax;
  	scanf("%d", &smax);
  	char s[smax+1];
  	scanf("%s", s);
  	int pre_seat = 0;
  	int this_seat = 0;
  	int to_add = 0;
  	for(int rr=0;rr<smax+1;rr++){
  		this_seat = s[rr] - '0';
  		if (this_seat > 0){
	  		if(pre_seat + to_add < rr){
	  			to_add = to_add + (rr - (pre_seat + to_add));   			
	  		}
  		}
  		pre_seat += this_seat;
  	}
		printf("Case #%d: %d", case_index,to_add);
		if(case_index <= 99){
			printf("\n");
		}		
  case_index += 1;
  }
	return 0;
}