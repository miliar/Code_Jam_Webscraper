#include <cstdio>
#include <algorithm>
using namespace std;

const int H = 1 << 0;
const int B = 1 << 1;
const int D = 1 << 2;
const int G = 1 << 3;

char tab[100][101];
int interdit[100][101];

void main2()
{
  int nblin, nbcol;
  scanf("%d%d", &nblin, &nbcol);
  
  for (int i=0; i<nblin; i++)
    scanf("%s", tab[i]);
  
  for (int i=0; i<nblin; i++)
  for (int j=0; j<nbcol; j++)
    interdit[i][j] = 0;
  
  for (int i=0; i<nblin; i++)
  {
    for (int j=0; j<nbcol; j++)
    if (tab[i][j] != '.')
    {
      interdit[i][j] |= G;
      break;
    }
  }
  
  for (int i=0; i<nblin; i++)
  {
    for (int j=nbcol-1; j>=0; j--)
    if (tab[i][j] != '.')
    {
      interdit[i][j] |= D;
      break;
    }
  }
  
  for (int j=0; j<nbcol; j++)
  {
    for (int i=0; i<nblin; i++)
    if (tab[i][j] != '.')
    {
      interdit[i][j] |= H;
      break;
    }
  }
  
  for (int j=0; j<nbcol; j++)
  {
    for (int i=nblin-1; i>=0; i--)
    if (tab[i][j] != '.')
    {
      interdit[i][j] |= B;
      break;
    }
  }
  
  for (int i=0; i<nblin; i++)
  for (int j=0; j<nbcol; j++)
  {
    
    if (interdit[i][j] == (H | B | G | D))
    {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  
  int res = 0;
  for (int i=0; i<nblin; i++)
  for (int j=0; j<nbcol; j++)
  {
    if (tab[i][j] == '^' && interdit[i][j] & H) res++;
    if (tab[i][j] == 'v' && interdit[i][j] & B) res++;
    if (tab[i][j] == '>' && interdit[i][j] & D) res++;
    if (tab[i][j] == '<' && interdit[i][j] & G) res++;
  }
  
  printf("%d\n", res);
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int i=1; i<=T; i++)
  {
    printf("Case #%d: ", i);
    main2();
  }
}
