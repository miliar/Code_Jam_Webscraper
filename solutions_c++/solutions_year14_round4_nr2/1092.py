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
int n, a[1000];
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    cin >> n;
    for (int i = 0; i < n; ++i)
      cin >> a[i];
    int ret = 1000000000;
    vector<int> v;
    for (int i = 0; i < n; ++i)
      v.push_back(i);
    do {
      int inc = 1;
      bool bad = false;
      for (int i = 0; i+1 < n; ++i) {
	if (inc && (a[v[i]] < a[v[i+1]])) continue;
	else if (a[v[i]] > a[v[i+1]]) inc = 0;
	else { bad = true; break; }
      }
      if (!bad) {
	int z = 0;
	for (int i = 0; i < n; ++i)
	  for (int j = i+1; j < n; ++j)
	    if (v[i] > v[j]) ++z;
	ret = min(ret, z);
      }
    } while(next_permutation(v.begin(), v.end()));
    printf("Case #%d: %d\n", rr, ret);
  }
  return 0;
}
