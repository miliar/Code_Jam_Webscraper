#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

int solve(int n) {
  unordered_set<int> was;
  for (int i = 1; i < 1000; i++) {
    for (int x = i * n; x; x /= 10) {
      was.insert(x % 10);
    }
    if (sz(was) == 10) {
      return i * n;
    }
  }
  return -1;
}

void testCase()
{
  int n;
  scanf("%d", &n);
  int ans = solve(n);
  if (ans == -1) {
    printf("INSOMNIA\n");
  } else {
    printf("%d\n", ans);
  }
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
//  for (int n = 1; n <= 1000000; n++) {
//    assert(solve(n) != -1);
//  }

  int T;
//  cin >> T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d: ", t);
    testCase();
  }
  return 0;
}
