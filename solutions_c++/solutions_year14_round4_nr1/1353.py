
#include <cstring>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>

using namespace std;


int N, X;

int sizes[100000];

void solve(int CASE) {
  cin >> N >> X;
  for (int i = 0; i < N; ++i) {
    cin >> sizes[i];
  }

  std::sort(sizes, sizes+N);

  int discs = 0;
  int i = 0, j = N-1;
  while(i <= j) {
    //fprintf(stderr, "%d %d\n", i, j);
    if (i == j) {
      discs++;
      break;
    }

    if (sizes[i] + sizes[j] <= X) {
      discs++;
      i++;
      j--;
    } else {
      discs++;
      j--;
    }
  }

  printf("Case #%d: %d\n", CASE, discs);
}

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i)
    solve(i+1);

  return 0;
}

