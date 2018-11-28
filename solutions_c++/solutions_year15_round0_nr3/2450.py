#include <bits/stdc++.h>

using namespace std;

const int UM = 1, I = 2, J = 3, K = 4;

int MAT[5][5] = {{0,0,0,0,0},
                  {0,UM, I, J, K},
                  {0, I, -UM, K, -J},
                  {0, J, -K, -UM, I},
                  {0, K, J, -I, -UM}};

int mult(int a, int b) {
  if ((a > 0) == (b > 0)) return MAT[abs(a)][abs(b)];
  else return -MAT[abs(a)][abs(b)];
}

char str[10005];
int arr[10005], st[40005], n;

void build(int no = 1, int l = 0, int r = n-1) {
  if (l == r) {
    st[no] = arr[l]; return;
  }
  int nl = no + no, nr = nl + 1, mid = (l + r) >> 1;
  build(nl, l, mid);
  build(nr, mid+1, r);
  st[no] = mult(st[nl], st[nr]);
}

int query(int i, int j, int no = 1, int l = 0, int r = n-1) {
  if (j < l || i > r) return UM;
  if (i <= l && r <= j) return st[no];
  int nl = no + no, nr = nl + 1, mid = (l + r) >> 1;
  int a = query(i, j, nl, l, mid);
  int b = query(i, j, nr, mid+1, r);
  return mult(a,b);
}

int from_left[10005], from_right[10005];
int pos_left[10005], pos_right[10005];
int left_sz, right_sz;

int query_bf(int i, int j) {
  int now = UM;
  for (int x = i; x <= j; ++x) {
    now = mult(now, arr[x]);
  }
  return now;
}

int main() {
  int nt; scanf("%d", &nt);
  for (int _ = 1; _ <= nt; ++_) {
    int l, x; scanf("%d %d", &l, &x);
    scanf("%s", str);
    n = 0;
    for (int i = 0; i < x; ++i) {
      for (int j = 0; str[j]; ++j) {
        if (str[j] == 'i') arr[n++] = I;
        else if (str[j] == 'j') arr[n++] = J;
        else arr[n++] = K;
      }
    }
    build();
    left_sz = 0;
    right_sz = 0;
    int now = UM;
    for (int i = 0; i < n; ++i) {
      now = mult(now, arr[i]);
      from_left[i] = now;
      if (from_left[i] == I) {
        pos_left[left_sz++] = i;
      }
    }
    now = UM;
    for (int i = n-1; i >= 0; --i) {
      now = mult(arr[i], now);
      from_right[i] = now;
      if (from_right[i] == K) {
        pos_right[right_sz++] = i;
      }
    }
    bool ok = false;
    for (int i = 0; i < left_sz; ++i) {
      for (int j = 0; j < right_sz; ++j) {
        if (pos_left[i] > pos_right[j]) break;
        if (pos_left[i] + 1 > pos_right[j] - 1) continue;
        if (query(pos_left[i] + 1, pos_right[j] - 1) == J) {
          ok = true; goto lol;
        }
      }
    }
    lol:;
    if (ok) printf("Case #%d: YES\n", _);
    else printf("Case #%d: NO\n", _);
  }
  return 0;
}