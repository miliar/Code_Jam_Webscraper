#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

void solve(int CASE) {
  char data[1000];
  cin >> data;

  int n = strlen(data);
  int flips = data[n-1] == '-' ? 1 : 0;

  for (int i = 1; i < n; i++) {
    if (data[i] != data[i-1]) flips++;
  }

  printf("Case #%d: %d\n", CASE, flips);
}

int main() {
  int T;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    solve(i);
  }

  return 0;
}
