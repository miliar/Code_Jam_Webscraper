#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;

void main2()
{
  int nb_col, nb_lin, nb_mines;
  scanf("%d%d%d", &nb_lin, &nb_col, &nb_mines);
  
  if (nb_col * nb_lin == nb_mines + 1)
  {
    for (int i=0; i<nb_lin; i++)
    {
      for (int j=0; j<nb_col; j++)
        printf("%c", i+j ? '*' : 'c');
      printf("\n");
    }
    
    return;
  }
  
  int tab[nb_lin+1];
  for (int i=0; i<=nb_lin; i++)
    tab[i] = 0;
  tab[0] = 1;
  
  while (tab[nb_lin] == 0)
  {
    int inf=0, sup=nb_lin-1;
    while (tab[inf] == 0) inf++;
    while (tab[sup] == 0) sup--;
    while (sup > 0 && tab[sup-1] != 0) sup--;
    //printf("%d %d\n", inf, sup);
    if (inf == sup)
    {
      int M = 0;
      for (int i=0; i<nb_lin; i++)
      {
        int l = tab[i];
        if (i > 0) l = max(l, tab[i-1]);
        if (i < nb_lin-1) l = max(l, tab[i+1]);
        
        if (l == 0) l = -1;
        if (l == nb_col) l = nb_col - 1;
        
        M += nb_col - l - 1;
      }
      
      if (nb_mines == M)
      {
        bool debut = false;
        for (int i=0; i<nb_lin; i++)
        {
          int l = tab[i];
          if (i > 0) l = max(l, tab[i-1]);
          if (i < nb_lin-1) l = max(l, tab[i+1]);
          
          if (l == 0) l = -1;
          if (l == nb_col) l = nb_col - 1;
          
          for (int j=0; j<=l; j++)
            if (j <= tab[i] && !debut) { printf("c"); debut = true; }
            else printf(".");
          for (int j=l+1; j<nb_col; j++) printf("*");
          printf("\n");
        }
        
        return;
      }
    }
    
    tab[0]++;
    for (int i=0; tab[i] == nb_col+1; i++)
    {
      tab[i+1]++;
      tab[i] = 0;
    }
  }
  
  printf("Impossible\n");
}

int main()
{
  int N;
  scanf("%d", &N);
  
  for (int i=0; i<N; i++)
  {
    printf("Case #%d:\n", i+1);
    main2();
  }
}
