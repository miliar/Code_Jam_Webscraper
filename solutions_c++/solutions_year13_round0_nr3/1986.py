#include <algorithm>
#include <functional>

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <string>
#include <vector>

using namespace std;

typedef long long llint;

bool is_palindrome(llint x) {
  static char buff[123]; sprintf(buff, "%lld", x);
  int len = strlen(buff);
  for (int a = 0, b = len-1; a < b; ++a, --b)
    if (buff[a] != buff[b])
      return false;
  return true;
}

int main(void)
{
  vector<llint> good;

  for (llint i = 1; i*i <= 10e14; ++i) {
    if (is_palindrome(i) && is_palindrome(i*i)) {
      good.push_back(i*i);
    }
  }

  int T; scanf("%d", &T);

  for (int counter = 0; counter < T; ++counter) {
    llint a, b; scanf("%lld %lld", &a, &b);
    int cnt = 0;
    for (int i = 0; i < (int)good.size(); ++i) {
      if (a <= good[i] && good[i] <= b)
        ++cnt;
    }

    printf("Case #%d: %d\n", counter + 1, cnt);
    fflush(stdout);
  }

  return (0-0);
}
