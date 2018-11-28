#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#define MAX 1024
char s[MAX];

int main(void)
{
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    int n, tot, r;
    scanf("%d %s", &n, s);
    tot = r = 0;
    for(int i = 0; i <= n; i++)
    {
      if (tot < i)
      {
        r += i-tot;
        tot = i;
      }
      tot += (int)(s[i]-'0');
    }

    printf("Case #%d: %d\n", caso, r);
  }
}
