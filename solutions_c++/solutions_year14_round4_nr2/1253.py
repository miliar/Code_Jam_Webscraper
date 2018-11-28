
#include <cstring>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>

using namespace std;


int N, X;

int val[1000];
int sorted[1000];
int backup[1000];
int expected[1000];
int indices[1000];

int nup, ndown;
int up[1000];
int down[1000];

int crossings() {
  for (int i = 0; i < N; ++i) {
    int closest = N*N;
    for (int j = 0; j < N; ++j) if (expected[j] == val[i] && abs(i-j) < abs(i-closest)) closest = j;

    indices[i] = closest;
  }

  int c = 0;
  for (int i = 0; i < N; ++i) {
    for (int j = i+1; j < N; ++j) {
      if (indices[j] < indices[i]) {
        //fprintf(stderr, "%d(%d) crosses with %d(%d)\n", val[i], i, val[j], j);
        c++;
      }
    }
  }

  return c;
}

void process() {
}


void solve(int CASE) {
  cin >> N;

  nup = 0;
  ndown = 0;

  for (int i = 0; i < N; ++i) {
    int v;
    cin >> v;
    val[i] = sorted[i] = backup[i] = v;

    bool found = false;
    for (int j = 0; j < nup; ++j) if (up[j] == v) { found = true; break; }
    if (found) down[ndown++] = v;
    else up[nup++] = v;
  }

  if (N == 1) {
    printf("Case #%d: %d\n", CASE, 0);
    return;
  }

  std::sort(sorted, sorted+N);
  std::sort(up, up+nup);
  std::sort(down, down+ndown);


  for (int i = 0; i < nup; ++i) expected[i] = up[i];
  for (int i = 0; i < ndown; ++i) expected[i+nup] = down[ndown - i - 1];
  //for (int i = 0; i < N; ++i) printf("%d ", val[i]); puts("");


  std::sort(expected, expected+N);
  int c = N*N;
  do {
    int same = 0;
    int s = expected[0] - expected[1];
    for (int i = 1; i < N; ++i) {
      int s2 = expected[i-1] - expected[i];
      if (s2 == 0) { same = 1; break; }
      if (s2 < 0 && s > 0) { same = 1; break; }
      s = s2;
    }

    if (!same) {
      int k = crossings();
      if (k < c) {
        //for (int i = 0; i < N; ++i) printf("%d ", expected[i]); puts("");
        c = k;
      }
    }
  } while(std::next_permutation(expected, expected+N));



  printf("Case #%d: %d\n", CASE, c);
}

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i)
    solve(i+1);

  return 0;
}

