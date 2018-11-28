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
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std; 

int t;
string s;
int n, cc, lcc;
long long res;

bool v[255];

int main() {
  memset(v, 1, sizeof(v));
  v['a'] = v['e'] = v['i'] = v['o'] = v['u'] = false;
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
  scanf ("%d", &t);
  for (int c = 0; c < t; c++) {
    cin >> s >> n;
    res = 0LL;
    cc = lcc = 0;
    for (int i = 0; i < s.size(); i++) {
      if (v[s[i]] == true) {
        cc++;
      } else {
        cc = 0;
      }
      if (cc >= n) {
        res += 1;
        res += (long long)s.size() - i - 1;
        res += max(0LL, (long long)(max(0, i - n + 1) - max(0, lcc - n + 2)) * (long long)(s.size() - i));
        lcc = i;
      }
    }
    printf("Case #%d: %lld\n", c + 1, res);
  }
	return 0;
}