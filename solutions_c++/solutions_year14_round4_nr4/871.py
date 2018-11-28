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
int n, m, put[8], biggest, ret;
string S[8];
int calc() {
  int q = 0;
  for (int i = 0; i < n; ++i) {
    set<string> z = set<string>();
    for (int j = 0; j < m; ++j)
      if (put[j] == i)
	for (int l = 0; l <= S[j].size(); ++l)
	  z.insert(S[j].substr(0, l));
    q += z.size();
  }
  return q;
}
void go(int at) {
  if (at == m) {
    int x = calc();
    if (x == biggest)
      ++ret;
    else if (x > biggest)
      biggest = x, ret = 1;
  } else {
    for (int i = 0; i < n; ++i) {
      put[at] = i;
      go(at+1);
    }
  }
}
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    cin >> m >> n;
    biggest = 0;
    ret = 0;
    for (int i = 0; i < m; ++i)
      cin >> S[i];
    go(0);
    printf("Case #%d: %d %d\n", rr, biggest, ret);
  }
  return 0;
}
