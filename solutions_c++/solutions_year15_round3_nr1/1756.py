#include <stdio.h>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

int main(void) {
  int numCases;
  cin >> numCases;

  for (int cases = 1; cases <= numCases; cases++) {
    int R, C, W;
    cin >> R >> C >> W;

    //Stage1
    int ret = C / W - 1 > 0 ? C / W - 1 : 0;
    //Stage2
    ret += W;
    ret += C % W ? 1 : 0;
    ret *= R;
    printf("Case #%d: %d\n", cases, ret);
  }

  return 0;
};
