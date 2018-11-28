#include <cstdio>
#include <algorithm>
using namespace std;

int tab[1000];
int mini[100];
int maxi[100];

void main2()
{
  int N, K;
  scanf("%d%d", &N, &K);
  
  for (int i=0; i<N-K+1; i++)
    scanf("%d", &tab[i]);
  
  for (int i=0; i<K; i++)
  {
    mini[i] = 0;
    maxi[i] = 0;
    int act = 0;
    for (int j=0; i+(j+1)*K<N; j++)
    {
      act += tab[i+1+j*K] - tab[i+j*K];
      mini[i] = min(mini[i], act);
      maxi[i] = max(maxi[i], act);
    }
  }
  
  long long int inf = 0;
  long long int sup = 1000000000;
  while (sup - inf > 0)
  {
    int med = (inf + sup) / 2;
    long long int m = 0;
    long long int M = 0;
    bool error = false;
    for (int i=0; i<K; i++)
    {
      m -= mini[i];
      M += med - maxi[i];
      if (maxi[i] - mini[i] > med)
        error =  true;
    }
    
    //printf("%d : %d %d\n", med, m, M);
    
    if (m > M && !error) printf("Noooo\n");
    
    long long int x = (tab[0] - m) / K;
    if (m + K*x > tab[0]) x--;
    
    if (m + K*x <= tab[0] && tab[0] < m + K*(x+1)){} else printf("Nooo\n");
    
    //printf("%d : %d %d %d %d\n", med, m, tab[0], M, K);
    //printf("%d : %d %d %d\n", med, m + K*x, tab[0], M + K*x);
    
    if (tab[0] > M + K*x) error = true;
    
    if (error)
      inf = med+1;
    else
      sup = med;
  }
  
  printf("%lld\n", inf);
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
