#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;
string s;
int N;
int INF = 1000000000;
int reach[1000001];
int next[1000001];
inline char isvow(char c) { return c=='a'||c=='e'||c=='i'||c=='o'||c=='u'; }
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    cin >> s >> N;
    int n = s.size();
    for (int i = 0; i < n; ++i) reach[i] = -1, next[i] = -1;
    for (int i = n - 1; i >= 0; --i) {
      if (isvow(s[i])) continue;
      else if (i==n-1 || isvow(s[i+1])) reach[i] = i;
      else reach[i] = reach[i+1];
    }
    for (int i = 0; i < n; ++i)
      if (reach[i]-i+1 < N)
	s[i] = 'a', reach[i] = -1;
    for (int i = n - 1; i >= 0; --i)
      if (!isvow(s[i])) next[i] = i;
      else if (i==n-1) continue;
      else next[i] = next[i+1];
    int ret = 0;
    for (int i = 0; i < n; ++i)
      if (next[i] != -1)
	ret += n - (next[i]+N-1);
    printf("Case #%d: %d\n", rr, ret);
  }
  return 0;
}
