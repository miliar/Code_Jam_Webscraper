#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;


long long n, p;
long long total;

inline bool isgood1(long long i) {
  long long maxlooses = i;
  long long place = total - 1;
  for (long long j = 0; j < n; j++)
  {
    if (maxlooses == 0)
      place -= (1ll << (n - 1 - j));
    maxlooses = (maxlooses -  1) / 2;
  }
  
  return (place < p);
}

inline bool isgood2(long long i) {
  long long maxwin = total - 1 - i;
  long long place = 0;
  for (long long j = 0; j < n; j++)
  {
    if (maxwin == 0)
      place += (1ll << (n - 1 - j));
    maxwin = (maxwin - 1) / 2;
  }
  
  return (place < p);
}

void solve() {
  cin >> n >> p;
  
  total = 1ll << n;
  
  long long l = 0;
  long long r = total;
  while (r - l > 1) {
    long long m = l + (r-l)/2;
    if (isgood1(m))
      l = m;
    else
      r = m;
  }
  cout << l << ' ';
  
  l = 0;
  r = total;
  while (r - l > 1) {
    long long m = l + (r-l)/2;
    if (isgood2(m))
      l = m;
    else
      r = m;
  }
  
  cout << l << endl;
}

int main() {
  
  #ifdef OFFLINE
  freopen("B_input.txt","r", stdin);
  freopen("B_output.txt","w", stdout);
  #endif
  int t;
  scanf("%d\n", &t);
  for (int testnum = 0; testnum < t; testnum++) {
    printf("Case #%d: ", testnum + 1);
    solve();
  }
}
