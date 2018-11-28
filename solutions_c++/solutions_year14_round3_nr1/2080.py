#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <tuple>
#include <cmath>

#define MAX 40
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    int P, Q;
    scanf("%d/%d", &P, &Q);

    int count = 0;
    bool possible = false;
    int q = Q;
    while (true) {
      if (q % 2 != 0) {
        break;
      }
      q = q / 2;
      count++;
      if (q == P || q == 1) {
        possible = true;
        break;
      }
    }
    count = 0;
    if (possible) {
      while (true) {
        if (P * pow(2, count) >= Q) {
          break;
        }
        count++;
      }
    }


    //    printf("%d/%d\n", P, Q);
    //    printf("count %d\n", count);
    if (possible) {
      printf("Case #%d: %d\n", t, count);
    } else {
      printf("Case #%d: impossible\n", t);
    }

  }
}
