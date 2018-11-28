#include <stdio.h>
#include <vector>
using namespace std;
void solve_case()
{
  int p;
  std::vector<int> poss, sel;

  scanf("%d", &p);
  int tmp;
  for (int i = 0; i< 4 ;i++)
    {
      for (int j = 0; j < 4 ; j++)
        {
          scanf("%d", &tmp);
          if (p == i+1)
            {
              poss.push_back(tmp);
            }
        }
    }
  scanf("%d", &p);
  for (int i =0; i< 4; i++)
    {
      for (int j =0; j < 4 ; j++)
        {
          scanf("%d",&tmp);
          if (p == i+1)
            {
              for (int k = 0; k < poss.size(); k++)
                {
                  if (poss[k] == tmp)
                    {
                      sel.push_back(tmp);
                      break;
                    }
                }
            }
        }
    }
  if (sel.size() == 0)
    {
      printf("Volunteer cheated!\n");
    }
  else
    {
      if (sel.size() > 1)
        {
          printf ("Bad magician!\n");
        }
      else
        {
          printf("%d\n", sel[0]);
        }
    }
}

int main()
{
  int T = 0;
  scanf("%d", &T);
  for (int i = 0; i < T; i++)
    {
      printf ("Case #%d: ", i+1);
      solve_case();
    }
}
