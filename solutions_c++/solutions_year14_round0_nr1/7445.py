/*
 * main.cpp
 *
 *  Created on: 2014年4月12日
 *      Author: maxiao04
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main() {
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T, res, num[16];
  map<int, int> a, b;
  scanf("%d\n", &T);
  for (int tc = 0; tc < T; tc += 1) {
    printf("Case #%d: ", tc + 1);
    a.clear();
    b.clear();
    scanf("%d", &res);
    for (int i = 0; i < 16; i += 1) {
      scanf("%d", &num[i]);
    }
    for (int i = (res - 1) * 4, j = 0; j < 4; i += 1, j += 1) {
      a[num[i]] = 1;
    }

    scanf("%d", &res);
    for (int i = 0; i < 16; i += 1) {
      scanf("%d", &num[i]);
    }
    for (int i = (res - 1) * 4, j = 0; j < 4; i += 1, j += 1) {
      b[num[i]] = 1;
    }

    int n;
    res = 0;
    for (map< int, int >::iterator it = a.begin(); it != a.end(); ++it) {
      if (b.find(it->first) != b.end()) {
        res += 1;
        n = it->first;
      }
    }

    if (res == 0) {
      printf("Volunteer cheated!");
    }
    else if (res == 1) {
      printf("%d", n);
    }
    else {
      printf("Bad magician!");
    }

    printf("\n");
  }

  return 0;
}
