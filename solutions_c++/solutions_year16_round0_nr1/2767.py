#include <cstring>
#include <iostream>
#include <set>

using namespace std;

int T, N, c;
set<long long> visited;
bool seen[10];

void setSeen(long long n) {
  while (n) {
    if (!seen[n % 10])
      c++;
    seen[n % 10] = true;
    n /= 10;
  }
}

long long go(long long n) {
  visited.clear();
  memset(seen, false, sizeof(seen));
  c = 0;
  long long curr = n;
  while (true) {
    if (visited.find(curr) != visited.end())
      return -1;
    visited.insert(curr);
    setSeen(curr);
    if (c == 10)
      return curr;
    curr += n;
  }
  return 0;
}

int main() {
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    scanf("%d", &N);
    long long res = go(N);
    if (res < 0) {
      printf("Case #%d: INSOMNIA\n", i);
    } else {
      printf("Case #%d: %lld\n", i, res);
    }
  }
  return 0;
}
