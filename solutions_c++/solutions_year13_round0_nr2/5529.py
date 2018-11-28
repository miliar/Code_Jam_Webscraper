#include <cstdio>
 
const int SIZE = 100;
 
int sX, sY;
int terrain[SIZE][SIZE];
bool ok[SIZE][SIZE];
 
void tester(int x, int y, int dX, int dY)
{
  int curX = x+dX;
  int curY = y+dY;
  int maximum = terrain[x][y];
  
  while (curX < sX && curY < sY)
  {
    if (terrain[curX][curY] > maximum)
      maximum = terrain[curX][curY];
    curX += dX;
    curY += dY;
  }
  
  curX = x;
  curY = y;
  
  while (curX < sX && curY < sY)
  {
    if (terrain[curX][curY] == maximum)
      ok[curX][curY] = true;
    curX += dX;
    curY += dY;
  }
  
}
 
void jouer()
{
  scanf("%d%d", &sY, &sX);
  
  for (int y = 0; y < sY; ++y)
  for (int x = 0; x < sX; ++x)
  {
    scanf("%d", &terrain[x][y]);
    ok[x][y] = false;
  }
  
  for (int y = 0; y < sY; ++y)
    tester(0,y,1,0);
  for (int x = 0; x < sX; ++x)
    tester(x,0,0,1);
  
  for (int y = 0; y < sY; ++y)
  for (int x = 0; x < sX; ++x)
    if (!ok[x][y])
    {
      printf("NO");
      return;
    }
  
  printf("YES");
}
 
int main()
{
  int nbJeux;
  scanf("%d", &nbJeux);
  
  for (int iJeu = 1; iJeu <= nbJeux; ++iJeu)
  {
    printf("Case #%d: ", iJeu);
    jouer();
    printf("\n");
  }
  
  return 0;
}