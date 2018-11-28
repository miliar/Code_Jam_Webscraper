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
  freopen("A-large.in", "r", stdin);
  freopen("answer.out", "w", stdout);
  int T;
  cin>>T;
  for(int t = 1; t <= T; t++){
	  int sm;
	  string an;
	  cin>>sm>>an;
	  int s = 0, ans = 0;
	  for(int i = 0; i <= sm; i++){
		  int add = max(0, i - s);
		  ans += add;
		  s += an[i] - '0';
		  s += add;
	  }
	  cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}
