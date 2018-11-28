#include <cstdio>

const int SIZE = 4;
const char EMPTY = '.';
const char NONE = 'T';

char squares[SIZE][SIZE];

bool tester(int y, int x, int dirY, int dirX)
{
  char winner = squares[y][x];
  int nY = y+dirY;
  int nX = x+dirX;
  
  if (winner == NONE)
    winner = squares[nY][nX];
  
  if (winner == EMPTY)
    return false;
  
  for (int i = 1; i < 4; ++i)
  {
    if (squares[nY][nX] != winner && squares[nY][nX] != NONE)
      return false;
    nY += dirY;
    nX += dirX;
  }
  
  printf("%c won\n", winner);
  return true;
}

void solve(int iJeu)
{
  printf("Case #%d: ", iJeu);
  
  bool draw = true;
  for (int y = 0; y < SIZE; ++y)
    scanf("%s", squares[y]);
  
  for (int y = 0; y < SIZE && draw; ++y)
  for (int x = 0; x < SIZE; ++x)
    if (squares[y][x] == EMPTY)
    {
      draw = false;
      break;
    }
  
  for (int y = 0; y < SIZE; ++y)
    if (tester(y,0,0,1))
      return;
  
  for (int x = 0; x < SIZE; ++x)
    if (tester(0,x,1,0))
      return;
  
  if (tester(0,0,1,1))
      return;
  
  if (tester(3,0,-1,1))
      return;
  
  if (draw)
    printf("Draw\n");
  else
    printf("Game has not completed\n");
}

int main()
{
  int nbJeux;
  scanf("%d", &nbJeux);
  
  for (int iJeu = 1; iJeu <= nbJeux; ++iJeu)
    solve(iJeu);
  
  return 0;
}
