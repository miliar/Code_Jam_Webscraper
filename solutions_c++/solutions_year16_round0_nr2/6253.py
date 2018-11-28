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

int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    string s;
    getline(cin, s);
    int ret = 0;
    for (int i = 0; i+1<s.size(); ++i)
      if (s[i] != s[i+1])
	ret++;
    if ((s[0]=='-' && (ret%2==0)) || (s[0]=='+' && (ret%2==1)))
      ++ret;
    printf("Case #%d: %d\n", rr, ret);
  }
  return 0;
}
