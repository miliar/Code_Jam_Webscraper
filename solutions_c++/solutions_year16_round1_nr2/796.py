#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>

using namespace std;

struct Row {
  int a[128];
};

Row a[256];
bool u[256];
int N, skipR, skipC, missH;
int f[128][128];
int hh[2555];
bool rev;

void findmiss() {
  skipR = -1;
  skipC = -1;
  memset(hh, 0, sizeof(hh));
  for (int i = 1; i < N; i++) {
    hh[a[0].a[i]] += 1;
    hh[a[1].a[i]] += 1;
  }
  for (int i = 2; i < 2 * N - 1; i++) {
    hh[a[i].a[0]] -= 1;
  }
  missH = -1;
  for (int i = 0; i <= 2500; i++)
    if (hh[i])
      missH = i;
  for (int i = 1; i < N; i++) {
    if (a[0].a[i] == missH) skipC = i;
    if (a[1].a[i] == missH) skipR = i;
  }
}

void fillR(int row, int index) {
  for (int i = 0; i < N; i++) {
    f[row][i] = a[index].a[i];
  }
}

void fillC(int col, int index) {
  for (int i = 0; i < N; i++) {
    f[i][col] = a[index].a[i];
  }
}

bool checkR(int row, int index, int bound, int miss) {
  for (int i = 0; i < bound; i++) {
    if (i == miss) continue;
    if (f[row][i] != a[index].a[i]) return false;
  }
  return true;
}

bool checkC(int col, int index, int bound, int miss) {
  for (int i = 0; i < bound; i++) {
    if (i == miss) continue;
    if (f[i][col] != a[index].a[i]) return false;
  }
  return true;
}

bool cmp(const Row &a, const Row &b) {
  return a.a[0] < b.a[0];
}

bool cmpR(const Row &a, const Row &b) {
  return b.a[0] < a.a[0];
}

bool eq(const Row &a, const Row &b) {
  for (int i = 0; i < N; i++)
    if (a.a[i] != b.a[i]) return false;
  return true;
}

void search(int index, int rbound, int cbound, int missindex, char misstype) {
  if (index == 2 * N - 1) {
    if (misstype == 'X' && rbound == N - 1) {
      misstype = 'R';
      missindex = rbound;
    }
    if (misstype == 'X' && cbound == N - 1) {
      misstype = 'C';
      missindex = cbound;
    }
    if (misstype == 'R') {
      for (int i = 0; i < N; i++) {
        printf(" %d", f[missindex][rev ? N - i - 1 : i]);
      }
    } else if (misstype == 'C') {
      for (int i = 0; i < N; i++) {
        printf(" %d", f[rev ? N - i - 1 : i][missindex]);
      }
    }
    printf("\n");
    throw "find result";
  }
  if (checkR(rbound, index, cbound, (misstype == 'C') ? missindex : -1)) {
    fillR(rbound, index);
    search(index + 1, rbound + 1, cbound, missindex, misstype);
  }
  if (u[index] && checkC(cbound, index, rbound, misstype == 'R' ? missindex : -1)) {
    fillC(cbound, index);
    search(index + 1, rbound, cbound + 1, missindex, misstype);
  }
  if (rbound == skipR && misstype == 'X' && (rev ? (a[index].a[0] <= missH) : (a[index].a[0] >= missH))) {
    search(index, rbound + 1, cbound, rbound, misstype = 'R');
  }
  if (cbound == skipC && misstype == 'X' && (rev ? (a[index].a[0] <= missH) : (a[index].a[0] >= missH))) {
    search(index, rbound, cbound + 1, cbound, misstype = 'C');
  }

}

void solve() {
  scanf("%d\n", &N);
  for (int i = 0; i < 2 * N - 1; i++) {
    for (int j = 0; j < N; j++) {
      scanf("%d", &a[i].a[j]);
    }
  }
  sort(a, a + 2 * N - 1, cmp);
  rev = false;
  if (a[0].a[0] != a[1].a[0]) {
    rev = true;
    for (int i = 0; i < 2 * N - 1; i++) {
      reverse(a[i].a, a[i].a + N);
    }
    sort(a, a + 2 * N - 1, cmpR);
  }

  memset(u, 1, sizeof(u));
  for (int i = 0; i < 2 * N - 2; i++) {
    if (eq(a[i], a[i + 1])) u[i] = 0;
  }

  findmiss();

  fillR(0, 0);
  fillC(0, 1);
  try {
    search(2, 1, 1, -1, 'X');
  } catch(...) {

  }
}

int main() {
  int T;
  scanf("%d\n", &T);
  for (int i = 1; i <= T; i++) {
    printf("Case #%d:", i);
    solve();
  }
}
