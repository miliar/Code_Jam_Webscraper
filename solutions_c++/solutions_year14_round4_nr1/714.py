#include "bits/stdc++.h"

using namespace std;

int w[10007];

int main()
{
  int t;
  scanf("%d", &t);
  for(int tti=1; tti<=t; tti++)
  {
    int x, n;
    scanf("%d%d", &n, &x);
    for (int i=0; i<n; i++)
        scanf("%d", &w[i]);
    sort(w, w +n);
    int wynik=0;
    int licznikgorny=n-1;
    int i=0;
    for ( ; i<n; i++)
    {
        for ( ; licznikgorny!=i; licznikgorny--)
            if (w[i]+w[licznikgorny]<=x)
            {
                w[licznikgorny]=x;   
                break;
            }
        if (licznikgorny==i)
            break;
    }
    wynik += n-i;
    printf("Case #%d: %d\n",tti, wynik);
  }
  return 0;
}
