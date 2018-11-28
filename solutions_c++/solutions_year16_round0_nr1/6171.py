#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;

#define VI vector<int>

inline string print(VI x) {
  string s;
  for (int i = x.size()-1; i>=0; --i)
    s += string(1, x[i]+'0');
  return s;
}

inline VI strip(VI x) {
  VI z;
  int i = x.size()-1;
  while (i>=0 && !x[i]) --i;
  if (i == -1)
    return VI(0);
  for (int j = 0; j <= i; ++j)
    z.push_back(x[j]);
  return z;
}

inline VI mult(VI x, VI y) {
  VI ret = VI(x.size() + y.size(), 0);
  for (int i = 0; i < x.size(); ++i)
    for (int j = 0; j < y.size(); ++j)
      ret[i+j] += x[i]*y[j];
  for (int i = 0; i+1 < ret.size(); ++i) {
    ret[i+1] += ret[i]/10;
    ret[i] %= 10;
  }
  return strip(ret);
}

inline VI add(VI x, VI y) {
  VI ret = VI(max(x.size(), y.size())+1, 0);
  for (int i = 0; i < max(x.size(), y.size()); ++i)
    if (i >= x.size())
      ret[i] = y[i];
    else if (i >= y.size())
      ret[i] = x[i];
    else 
      ret[i] = x[i] + y[i];
  for (int i = 0; i+1 < ret.size(); ++i) {
    ret[i+1] += ret[i]/10;
    ret[i] %= 10;
  }
  return strip(ret);
}

inline VI convert(int x) {
  if (!x) return VI(0);
  VI z = VI();
  while (x) {
    z.push_back(x%10);
    x /= 10;
  }
  return z;
}

int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    int mask = 0;
    int x;
    cin >> x;
    if (!x) {
      printf("Case #%d: INSOMNIA\n", rr);
      continue;
    }
    int ticks = 0;
    VI at = convert(x);
    VI start = at;
    bool done = false;
    do {
      if (ticks > 10000000) break;
      for (int i = 0; i < at.size(); ++i)
	mask |= 1<<at[i];
      if (mask == 1023) {
	printf("Case #%d: %s\n", rr, print(at).c_str());
	done = true;
	break;
      } else
	at = add(at, start);
      ++ticks;
    } while(true);
    if (!done)
      printf("Case #%d: INSOMNIA\n", rr);
  }
  return 0;
}
