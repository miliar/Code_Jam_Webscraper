#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <set>
#include <stdio.h>
#include <vector>

using namespace std;

char s[1024];

int main() {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);

    scanf("%s", s);
    int l = strlen(s);

    string ret;
    for (int i = 0; i < l; ++i) {
      if (ret.length() == 0 || s[i] >= ret[0]) {
        ret = s[i] + ret;
      } else {
        ret += s[i];
      }
    }

    printf("%s\n", ret.c_str());
  }
}
