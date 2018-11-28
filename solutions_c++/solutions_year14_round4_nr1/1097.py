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
int n, x, done[10000];
vector<int> v;
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    cin >> n >> x;
    int y;
    memset(done, 0, sizeof(done));
    v = vector<int>();
    for (int i = 0; i < n; ++i) {
      cin >> y;
      v.push_back(y);
    }
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    int ret = 0;
    for (int i = 0; i < v.size(); ++i)
      if (!done[i]) {
	done[i] = 1;
	++ret;
	int j = i+1;
	while (j<v.size() && (done[j]||(v[j]+v[i]>x)))
	  ++j;
	if (j<v.size())
	  done[j] = 1;
      }
    printf("Case #%d: %d\n", rr, ret);
  }
  return 0;
}
