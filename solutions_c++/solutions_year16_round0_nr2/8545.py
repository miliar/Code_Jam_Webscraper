#include <stdio.h>
#include <algorithm>
#include <set>
#include <cmath>
#include <cstring>

#define MAX 101
using namespace std;

bool check(char a[])
{
  for (int i = 0; a[i] != '\0'; ++i)
    if (a[i] == '-')
      return false;
  return true;
}

int main() {
  //freopen("input.inp", "rt", stdin);
  //freopen("output.oup", "wt", stdout);   
  
  int t;
  char s[MAX];
  bool b[MAX];  
  int len, pos, last;
  int count;
  int c = 1;
  
  scanf("%d", &t);
  while (t--)
  {
    scanf("%s", s);
    len = strlen(s);
    count = 0;
    while (!check(s))
    {
      if (s[0] == '-')
      {
        pos = 0;
        while (s[pos] == '-')
        {
          s[pos] = '+';
          ++pos;
        }        
        reverse(s, s+pos);
        ++count;        
      }
      else
      {
        pos = 0;
        while (pos < len - 1)
        {
          if (s[pos] == '+')
          {
            s[pos] = '-';
            last = pos;
          }
          else
            break;
          ++pos;
        }        
        reverse(s, s+pos);
        ++count;        
      }
    }
    printf("Case #%d: %d\n", c, count);
    ++c;
  }
  
  return 0;
}