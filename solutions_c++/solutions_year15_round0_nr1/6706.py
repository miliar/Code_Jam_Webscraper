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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;
typedef long long ll;
const double PI = acos(-1.0);

int main()
{
  int t;
  cin >> t;
  
  for(int tcase = 1; tcase <= t; tcase++) {
    printf("Case #%d: ", tcase);
    
    int smax;
    string level;
    cin >> smax >> level;

    int c = level[0] - '0';
    int res = 0;
    for(int i = 0; i < smax; i++) {
      int n = level[i+1] - '0';
      if(c <= i) {
        res += i+1 - c;
        c = i+1;
      }
      c += n;
    }

    cout << res << endl;
  }

  return 0;
}
// Google Code Jam Problem A