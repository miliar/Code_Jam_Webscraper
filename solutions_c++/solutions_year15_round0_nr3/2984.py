#include <cstdlib>
#include <cstdio>
#include <vector>
using namespace std;

#define _1 1
#define _i 2
#define _j 3
#define _k 4

int mat[5][5] = {
  {0,  0,   0,   0,   0},
  {0, _1,  _i,  _j,  _k},
  {0, _i, -_1,  _k, -_j},
  {0, _j, -_k, -_1,  _i},
  {0, _k,  _j, -_i, -_1}
};

int charToVal(char q) {
  switch (q) {
  case '1': return _1;
  case 'i': return _i;
  case 'j': return _j;
  case 'k': return _k;
  }
}

int mult(int v1, int v2) {
  return mat[abs(v1)][abs(v2)] * (v1 * v2 > 0 ? 1 : -1);
}

bool solve(int L, int X, char* text) {
  vector<int> converted;
  for (int l = 0; l < L; l++) {
    converted.push_back(charToVal(text[l]));
  }
  vector<int> v;
  for (int x = 0; x < X; x++) {
    copy(converted.begin(), converted.end(), std::back_inserter(v));
  }
  /*for (int i = 0; i < v.size(); i++) {
    printf("%d", v[i]);
  }
  printf("\n");*/
  int a = 1;
  int split1 = -1;
  for (int i = 0; i < v.size(); i++) {
    if (a == _i) {
      split1 = i;
      break;
    }
    a = mult(a, v[i]);
  }
  a = 1;
  int split2 = -1;
  for (int i = v.size() - 1; i >= 0; i--) {
    a = mult(v[i], a);
    //printf("<%d, %d>", a, v[i]);
    if (a == _k) {
      split2 = i;
      break;
    }
  }
  a = 1;
  for (int i = split1; i < split2; i++) {
    a = mult(a, v[i]);
  }
  //printf("%d %d %d\n", split1, split2, a);
  return split1 != -1 && split2 != -1 && a == _j;
}

int main() {
  int T = 0;
  scanf("%d", &T);
  for (int t = 0; t < T; t++) {
    int L = 0, X = 0;
    scanf("%d %d", &L, &X);
    char line[10001];
    scanf("%s", line);
    printf("Case #%d: ", t + 1);
    if (solve(L, X, line))
      printf("YES");
    else
      printf("NO");
    printf("\n");
  }
  return 0;
}
