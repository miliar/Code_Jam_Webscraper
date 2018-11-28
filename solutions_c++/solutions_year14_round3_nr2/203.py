#include <cstdio>
#include <algorithm>
using namespace std;

const int MOD = 1000000007;

void main2()
{
  int N;
  scanf("%d", &N);
  
  char mot[N][101];
  int taille[N];
  for (int i=0; i<N; i++)
  {
    taille[i] = 0;
    scanf("%s", mot[i]);
    while (mot[i][taille[i]]) taille[i]++;
  }
  
  bool milieu[26];
  for (int c=0; c<26; c++)
  {
    milieu[c] = false;
    for (int i=0; i<N; i++)
    for (int j=0; j<taille[i]; j++)
    {
      if (mot[i][j] == 'a' + c)
      {
        int b = j;
        while (b < taille[i] && mot[i][b] == 'a' + c) b++;
        
        if (j != 0 && b != taille[i])
        {
          if (milieu[c])
          {
            printf("0\n");
            return;
          }
          milieu[c] = true;
        }
        
        j = b;
      }
    }
  }
  
  int tout[26], fin[26], debut[26];
  for (int c=0; c<26; c++)
  {
    tout[c] = 0;
    debut[c] = -1;
    fin[c] = -1;
    for (int i=0; i<N; i++)
    for (int j=0; j<taille[i]; j++)
    {
      if (mot[i][j] == 'a' + c)
      {
        int b = j;
        while (b < taille[i] && mot[i][b] == 'a' + c) b++;
        
        if (j == 0 && b == taille[i])
          tout[c]++;
        else if (j == 0)
        {
          if (debut[c] != -1)
          {
            printf("0\n");
            return;
          }
          debut[c] = i;
        }
        else if (b == taille[i])
        {
          if (fin[c] != -1)
          {
            printf("0\n");
            return;
          }
          fin[c] = i;
        }
        
        j = b;
      }
    }
    
    if (milieu[c] && (tout[c] > 0 || debut[c] != -1 || fin[c] != -1))
    {
      printf("0\n");
      return;
    }
    
  }
  
  int suivant[26];
  for (int c=0; c<26; c++)
  {
    if (debut[c] != -1)
      suivant[c] = mot[debut[c]][taille[debut[c]]-1] - 'a';
    else
      suivant[c] = -1;
      
    //if (tout[c] > 0 || debut[c] != -1 || fin[c] != -1)
      //printf("\n%c -> %d %d %d %d", c + 'a', suivant[c], debut[c], tout[c], fin[c]);
  }
  
  long long int res = 1;
  
  int comp = 0;
  for (int c=0; c<26; c++)
  {
    bool racine = debut[c] != -1 || tout[c];
    for (int d=0; d<26; d++)
      if (suivant[d] == c)
        racine = false;
    
    if (racine)
    {
      comp++;
      int d = c;
      while (d != -1)
      {
        //printf("%c ", 'a' + d);
        for (int i=1; i<=tout[d]; i++)
        {
          res *= i;
          res %= MOD;
        }
        
        d = suivant[d];
      }
      
      //printf("\n");
    }
  }
  
  //printf("%lld %d\n", res, comp);
  
  if (comp == 0)
  {
    printf("0\n");
    return;
  }
  
  for (int i=1; i<=comp; i++)
  {
    res *= i;
    res %= MOD;
  }
  
  printf("%lld\n", res);
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
