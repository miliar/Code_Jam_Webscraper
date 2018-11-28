#include <cstdio>
using namespace std;

int main() 
{
    int tcase, val;
    scanf ("%d", &tcase);
    for (int k = 1 ; k <= tcase; k ++)
    {
          int before, after, hit = 0, result;
          int mapping[16] = {0};
          scanf ("%d", &before);
          before --;
          for (int i = 0 ; i < 4; i++)
              for (int j = 0 ; j < 4; j++) 
              {
                  scanf ("%d", &val);
                  if (i == before)
                     mapping[val-1] ++;
              }
                  
          scanf ("%d", &after);
          after--;
          for (int i = 0 ; i < 4; i++)
              for (int j = 0 ; j < 4; j++)
              {
                  scanf ("%d", &val);
                  if (i == after && mapping[val-1] > 0)
                  {
                     hit ++;
                     if (hit == 1)
                        result = val;
                  }
              }
                 
          if (hit > 1)
             printf ("Case #%d: Bad magician!\n", k);
          else if (hit == 1)
             printf ("Case #%d: %d\n", k, result);
          else
             printf ("Case #%d: Volunteer cheated!\n", k);                          
    }
    return 0;
}
