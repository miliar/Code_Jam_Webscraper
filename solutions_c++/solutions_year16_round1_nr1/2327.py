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
    string S;
    cin >> S;
    string ret = string(1, S[0]), a1, a2;
    for (int i = 1; i < S.size(); ++i) {
      a1 = ret + string(1, S[i]);
      a2 = string(1, S[i]) + ret;
      if (a1 < a2)
	ret = a2;
      else
	ret = a1;
    }
    printf("Case #%d: %s\n", rr, ret.c_str());

  }
  return 0;
}
