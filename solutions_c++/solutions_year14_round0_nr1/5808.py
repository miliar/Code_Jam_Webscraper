#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;

int c, sign;
inline void get_int(int& n) {
  n = 0;
  c = getchar_unlocked();
  sign = 1;
  while (c < '0' || c > '9') {
    if (c == '-') sign = -1;
    c = getchar_unlocked();
  }
  while (c >= '0' && c <= '9') {
    n = (n<<3) + (n<<1) + c - '0';
    c = getchar_unlocked();
  }
  n = sign*n;
}

int main() {
  int T;
  get_int(T);
  for (int t = 1; t <= T; t++) {
    int b1[4][4], b2[4][4], r1, r2;
    get_int(r1);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) get_int(b1[i][j]);
    }
    get_int(r2);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) get_int(b2[i][j]);
    }

    int freq[20] = {0};
    for (int j = 0; j < 4; j++) freq[b1[r1-1][j]]++;
    for (int j = 0; j < 4; j++) freq[b2[r2-1][j]]++;

    int c = 0;
    int v = 0;
    for (int i = 0; i < 20; i++) {
      if (freq[i] == 2) {
        c++;
        v = i;
      }
    }

    printf("Case #%d: ", t);
    if (c == 0) {
      printf("Volunteer cheated!\n");
    } else if (c == 1) {
      printf("%d\n", v);
    } else {
      printf("Bad magician!\n");
    }

  }
  return 0;
}