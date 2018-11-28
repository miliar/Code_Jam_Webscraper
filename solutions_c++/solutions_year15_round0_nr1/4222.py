#include <iostream>
#include <cstdio>
int solve()
{
  int n;
  std::cin >> n;
  int count = 0;
  int added = 0;
  std::string res;
  std::cin >> res;
  for (int i = 0; i < n+1; i++) {
    int x = res[i]-'0';
    if (count < i && x > 0) {
      added += (i-count);
      count = i;
    }
    count += x;
  }
  return added;
}

int main()
{
  int cases;
  std::cin >> cases;
  for (int i = 0; i < cases; i++) {
    std::cout << "Case #" << i+1 << ": " << solve() << std::endl;
  }
  return 0;
}
