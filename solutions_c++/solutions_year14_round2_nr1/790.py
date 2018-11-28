#include <cstdio>
#include <algorithm>
using namespace std;

void main2()
{
  int N;
  scanf("%d", &N);
  
  int taille[N];
  char mot[N][101];
  for (int i=0; i<N; i++)
  {
    scanf("%s", mot[i]);
    taille[i] = 0;
    while (mot[i][taille[i]]) taille[i]++;
  }
  
  int nb = 0;
  int tab[N][101];
  for (int i=0; i<N; i++)
  {
    int j=0, k=0;
    while (j < taille[i])
    {
      tab[i][k] = j;
      while (j+1 < taille[i] && mot[i][j] == mot[i][j+1]) j++;
      j++;
      k++;
    }
    tab[i][k] = j;
    
    if (nb != 0 && nb != k)
    {
      printf("Fegla Won\n");
      return;
    }
    nb = k;
  }
  
  int res = 0;
  for (int k=0; k<nb; k++)
  {
    char c = mot[0][tab[0][k]];
    for (int i=0; i<N; i++)
    {
      if (c != mot[i][tab[i][k]])
      {
        printf("Fegla Won\n");
        return;
      }
    }
    
    int best = 1000000000;
    for (int l=1; l<=100; l++)
    {
      int act = 0;
      for (int i=0; i<N; i++)
        act += abs(tab[i][k+1] - tab[i][k] - l);
      if (act < best) best = act;
    }
    
    res += best;
  }
  
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
