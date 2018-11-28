#include <cstdio>
#include <algorithm>
using namespace std;

void main2()
{
  int ligne1, ligne2;
  int grille1[4][4];
  int grille2[4][4];
  
  scanf("%d", &ligne1);
  for (int i=0; i<4; i++)
  for (int j=0; j<4; j++)
    scanf("%d", &grille1[i][j]);
  
  scanf("%d", &ligne2);
  for (int i=0; i<4; i++)
  for (int j=0; j<4; j++)
    scanf("%d", &grille2[i][j]);
  
  int nb = 0;
  int res = -1;
  for (int i=0; i<4; i++)
  for (int j=0; j<4; j++)
  if (grille1[ligne1-1][i] == grille2[ligne2-1][j])
  {
    nb++;
    res = grille1[ligne1-1][i];
  }
  
  if (nb == 0)
    printf("Volunteer cheated!\n");
  else if (nb > 1)
    printf("Bad magician!\n");
  else
    printf("%d\n", res);
}

int main()
{
  int N;
  scanf("%d", &N);
  
  for (int i=0; i<N; i++)
  {
    printf("Case #%d: ", i+1);
    main2();
  }
}
