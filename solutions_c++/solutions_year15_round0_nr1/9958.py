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
  int tt;
  cin >> tt;
  for (int qq=1;qq<=tt;qq++) {
    cout << "Case #" << qq << ":";
    int yy, cur, missing = 0, count = 0;
    char c;
    cin>>yy;
    for(int jj=0; jj<=yy; jj++){
      cin>>c;
      cur = c - '0';
      if(jj > count && cur > 0){
        missing += (jj - count);
        count += missing;
      }
      count += cur;
    }
    cout << " " << missing << endl;
  }
  return 0;
}
