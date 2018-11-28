#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
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

typedef long long i64;
const int N = 100000;

char g[N];



int main() {
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small-attempt0.out", "w", stdout);
  int T;
  //int ki = 0;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {

    //fflush(stdout);
    int n; i64 k;scanf("%d %s", &n, g);
    vector<int> digits;
    for(int  j =0; j < n+1 ; ++j)
    {
    	char temp = g[j];
    	digits.push_back(atoi(&temp));
    }
   // list<int> digits;
  //  splitNumber(digits,k);
    int minpeople = 0;
    int currpeople = 0;
    for(int i = 0; i < digits.size(); ++i)
    {

    	if(digits[i] != 0)
    	{

    		if( currpeople < i)
    		{
    		   minpeople += i - currpeople;
    		   currpeople += minpeople;
    		}
    		currpeople += digits[i];
    	}
    }

    printf("Case #%d: %d\n", Ti, minpeople);
    fflush(stdout);
    //if ((k + 1) % (1 << n) == 0) printf("Case #%d: %s\n", Ti, "ON");
    //else printf("Case #%d: %s\n", Ti, "OFF");
  }
   fflush(stdout);
  return 0;
}
