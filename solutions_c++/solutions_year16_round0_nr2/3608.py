#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

char toggle(char c) { return c == '+' ? '-' : '+'; }

int solve(string &s, int n, char need) {
  if (n == 0) {
    return 0;
  }

  char other = toggle(need);

  if (s[n - 1] == need) {
    return solve(s, n - 1, need);
  } else {
    return solve(s, n - 1, other) + 1;
  }
}

void testCase()
{
  string s;
  cin >> s;
  printf("%d\n", solve(s, sz(s), '+'));
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d: ", t);
    testCase();
  }
  return 0;
}
