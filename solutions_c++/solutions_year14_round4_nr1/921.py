#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <math.h>
#include <stack>
#include <queue>
#include <stdio.h>

using namespace std;

#define INF 0x3FFFFFFF

int n,x;
int s[20000];

int main() {
  int c;
  cin >> c;
  for (int cc = 1; cc <= c; cc++) {
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
      cin >> s[i];
    }
    sort(s, s+n);
    int res = 0;
    int lower = 0;
    int upper = n-1;
    int current = x;
    while (lower <= upper) {
      if (current == x) {
        current -= s[upper];
        upper--;
        res++;
      } else {
        if (current >= s[lower]) {
          lower++;
        }
        current = x;
      }
    }



    printf("Case #%d: %d\n", cc, res);
  }
  return 0;
}
