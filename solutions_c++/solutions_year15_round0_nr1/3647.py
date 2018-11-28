#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int Smax;
char c;

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%d ", &Smax);
    int standing = 0;
    int invited = 0;
    for (int s = 0; s <= Smax; ++s)
    {
      scanf("%c", &c);
      int count = c - '0';
      if (s > standing)
      {
        invited += s - standing;
        standing = s;
      }
      standing += count;
    }

    // output
    printf("Case #%d: %d\n", Ti, invited);
  }
  return 0;
}
