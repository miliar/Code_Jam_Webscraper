#include "bits/stdc++.h"

using namespace std;

int tab[10007];

int main()
{
  int t;
  scanf("%d", &t);
  for(int tti=1; tti<=t; tti++)
  {
    int n, a;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
      scanf("%d", &a);
      tab[i] = a;
    }
    int wsk1 = 0, wsk2 = n-1;
    long long wynik = 0;
    for(int i=0; i<n; i++)
    {
      int mini = 1000000007, wskmini = -1;
      for(int j=wsk1; j<=wsk2; j++)
        if(mini>tab[j])
        {
          mini = tab[j];
          wskmini = j;
        }
      int a = max(0, wskmini-wsk1),
          b = max(0, wsk2-wskmini);
      if(a<b)
      {
        wsk1++;
        wynik += a;
        tab[wskmini] = 1000000007;
        for(int j=wskmini; j>=wsk1; j--)
          swap(tab[j], tab[j-1]);
      }
      else
      {
        wsk2--;
        wynik += b;
        tab[wskmini] = 1000000007;
        for(int j=wskmini; j<=wsk2; j++)
          swap(tab[j], tab[j+1]);
      }
      //for(int j=0; j<n; j++)
      //  printf("%d ", tab[j]);
      //printf("\n");
    }
    printf("Case #%d: %lld\n",tti, wynik);
  }
  return 0;
}
