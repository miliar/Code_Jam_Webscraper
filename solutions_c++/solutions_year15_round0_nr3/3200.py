#include<cstdio>

using namespace std;

// 1 = 1
// i = 2
// j = 3
// k = 4
int times(int m, int n) {
  static int mat[5][5] = {
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2, -1, 4, -3},
    {0, 3, -4, -1, 2},
    {0, 4, 3, -2, -1}
  };
  int coe = 1;
  if (m < 0) {
    m = -m;
    coe *= -1;
  }
  if (n < 0) {
    n = -n;
    coe *= -1;
  }
  return coe * mat[m][n];
}

char toch[] = { 'x', '1', 'i', 'j', 'k' };

bool doit(int *arr, int *beg, int *end, int target, int cnt, int rept) {
  int r = 1;
  while (rept > 0) {
    while (arr != end) {
      r = times(r, *arr);
      arr++;
      if (cnt != 0 && target == r) {
        if (doit(arr, beg, end, target + 1, cnt - 1, rept)) {
          return true;
        }
      }
    }
    //arr ==end
    rept--;
    if (rept > 0) {
      arr = beg;
    }
  }
  if (cnt == 0 && target == r) {
    return true;
  }
  return false;
}

void run(int t) {
  int L;
  long long X;
  char cbuf[10001];
  int arr[10000];
  scanf("%d %lld", &L, &X);
  scanf("%s", cbuf);
  for (int i = 0; i < L; i++) {
    int r;
    switch(cbuf[i]) {
    case 'i': r = 2; break;
    case 'j': r = 3; break;
    case 'k': r = 4; break;
    }
    arr[i] = r;
  }
  printf("Case #%d: %s\n", t, doit((int*)arr, (int*)arr, (int*)arr + L, 2, 2, X) ? "YES" : "NO");
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    run(i);
  }
}
