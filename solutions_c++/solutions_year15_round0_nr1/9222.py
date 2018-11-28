#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char const *argv[])
{
  ios :: sync_with_stdio(false); cin.tie(NULL);
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i)
  {
    std::string p;
    int s;
    cin >> s >> p;
    int ep = 0;
    int a = 0;
    for (int i = 0; i <= s; ++i)
    {
      if(ep < i) {
        a += i - ep;
        ep += i - ep;
      }
      ep += p[i] - '0';
    }
    printf("Case #%d: %d\n", i+1, a);
  }
  return 0;
}
