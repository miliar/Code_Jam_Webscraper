#include <ctime>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>

using namespace std;

char s[20005];

int solve2(string s)
{
  vector<char> ss;
  for (int i = 0; i < s.size(); ++i)
  {
    if (ss.size() == 0)
    {
      ss.push_back(s[i]);
    }
    else
    {
      if (ss.back() == s[i])
      {
        ss.pop_back();
      }
      else
      {
        ss.push_back(s[i]);
      }
    }
  }

  return (s.size() * 5) - (ss.size() / 2) * 5;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int cn = 1; cn <= T; ++cn)
  {
    scanf("%s", s);
    printf("Case #%d: %d\n", cn, solve2(s));
  }
}
