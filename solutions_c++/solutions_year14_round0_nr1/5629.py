#include <iostream>
#include <cstring>
#include <cstdio>
#include <set>
using namespace std;


int main()
{
  int test;
  scanf("%d", &test);
  for (int t = 0; t < test; t++)
  {
    int row;
    scanf("%d", &row);
    --row;
    int tab[4][4];
    int T[32];
    memset(T, 0, sizeof(T));
    for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      scanf("%d", &tab[i][j]);
      
    for (int i = 0; i < 4; i++)
      T[tab[row][i]]++;
    scanf("%d", &row);
    --row;

    for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      scanf("%d", &tab[i][j]);
      
    for (int i = 0; i < 4; i++)
      T[tab[row][i]]++;
      
    int two = 0;
    int idx = -1;
    for (int i = 1; i <= 16; i++)
      if (T[i] == 2) {
        two++;
        idx = i;
      }
    printf("Case #%d: ", t+1);
    if (two == 1)
      printf("%d\n", idx);
    else if (two == 0)
      printf("Volunteer cheated!\n");
    else
      printf("Bad magician!\n");
    
    
    
    
  }
  
  return 0;
}
