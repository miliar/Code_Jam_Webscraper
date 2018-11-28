#include <stdio.h>
#include <set>

using namespace std;

int main()
{
  int n_cases;
  scanf("%d", &n_cases);
  for (int T = 0; T < n_cases; ++T)
  {
    int ccount = 0;
    set<int> s;
    int ans;
    for (int k = 0; k < 2; ++k)
    {
      int row;
      scanf("%d", &row);
      for (int i = 0; i < 16; ++i)
      {
        int num;
        scanf("%d", &num);
        if ((i / 4) == (row - 1))
        {
//          fprintf(stderr, "num = %d\n", num);
          if (k == 0)
          {
            s.insert(num);
          }
          else
          {
            if (s.find(num) != s.end())
            {
              ++ccount;
              ans = num;
            }
          }
        }
      }
    }
    printf("Case #%d: ", T + 1);
    if (ccount == 0)
      printf("Volunteer cheated!\n");
    else if (ccount == 1)
      printf("%d\n", ans);
    else
      printf("Bad magician!\n");
  }

  return 0;
}
