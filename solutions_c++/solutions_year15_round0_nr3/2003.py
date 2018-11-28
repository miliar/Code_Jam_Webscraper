#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int t[5][5] = {
  {0, 0,  0,  0,  0},
  {0, 1,  2,  3,  4},
  {0, 2, -1,  4, -3},
  {0, 3, -4, -1,  2},
  {0, 4,  3, -2, -1}
};

int res[10042][10042];

#define c(x) (2+(x)-'i')

int mult(int a, int b) {
  if (a<0 && b<0) return t[-a][-b];
  if (a<0) return -t[-a][b];
  if (b<0) return -t[a][-b];
  return t[a][b];
}

void build(char *s) {
  int len = strlen(s);
  for (int i = 0; i < len; ++i) {
    res[i][i] = c(s[i]);
    for (int j = i+1; j < len; ++j) {
      res[i][j] = mult(res[i][j-1], c(s[j]));
    }
  }
}

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int len, reps;
    cin >> len >> reps;
    char s[10042];
    scanf("%s", s);
    for (int i = 1; i < reps; ++i) {
      strncpy(s+(i*len), s, len);
    }
    s[len*reps] = 0;
    //cout << s << endl;

    build(s);

    len = strlen(s);

    for (int i = 1; i <= len-2; ++i) {
      for (int j = i+1; j <= len-1; ++j) {
        if (res[0][i-1] == 2 && res[i][j-1] == 3 && res[j][len-1] == 4) {
          cout << "Case #" << tt << ": YES\n";
          goto next;
        }
      }
    }

    cout << "Case #" << tt << ": NO\n";

    next:;
  }
}
