#include <cstdio>
#include <algorithm>
using namespace std;

int N, A[100], B[100], X[100], num[100], small[100];
int inc[100], dec[100];
int flag = 0;

int check (int idx) {
  if (idx == -1) return 1;
  inc[idx] = 1;
  for (int i = 0; i < idx; i++) {
    if (X[i] < X[idx] && inc[i] + 1 > inc[idx]) inc[idx] = inc[i] + 1;
  }
  if (inc[idx] != A[idx]) return 0;

  small[0] = -1;
  for (int i = 1; i <= N; i++)
    small[i] = small[i - 1] + 1 - num[i - 1];

  for (int i = idx; i >= 0; i--) {
    dec[i] = 1;
    for (int j = i + 1; j <= idx; j++) {
      if (X[i] > X[j] && dec[j] + 1 > dec[i]) dec[i] = dec[j] + 1;
    }
    if (dec[i] > B[i]) return 0;
    if (dec[i] + small[X[i]] < B[i]) return 0;
  }
  return 1;
}

void Search (int idx) {
  if (flag) return;
  if (!check (idx - 1)) return;
  if (idx == N) {
    for (int i = 0; i < N; i++) printf (" %d", X[i]);
    printf ("\n");
    flag = 1;
    return;
  }

  for (int i = 1; i <= N; i++) {
    if (num[i] == 0) {
      num[i] = 1;
      X[idx] = i;
      Search (idx + 1);
      num[i] = 0;
    }
  } 
}

int main ()
{
  freopen ("in.txt", "r", stdin);
  //freopen ("ou.txt", "w", stdout);
  int T; 
  scanf ("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf ("Case #%d:", i);
    scanf ("%d", &N);
    for (int j = 0; j < N; j++) scanf ("%d", A + j);
    for (int j = 0; j < N; j++) scanf ("%d", B + j);
    flag = 0;
    fill (num, num + 100, 0);
    Search (0);
  }
}

