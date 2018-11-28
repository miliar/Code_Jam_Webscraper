#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

const int MAXN=1000;

int n, t[MAXN+5];

void solve(int test)
{
  int n, p=0, wynik=1e9;

  scanf("%d", &n);
  for(int i=1; i<=n; i++)
  {
    scanf("%d", &t[i]);
    p=max(p,t[i]);
  }
  
  for(int i=1; i<=p; i++)
  {
    int akt=i;
    for(int j=1; j<=n; j++)
      akt+=(t[j]-1)/i;
    
    wynik=min(wynik,akt);
  }
  
  printf("Case #%d: %d\n", test, wynik);
}

int main()
{
  int q;
  scanf("%d", &q);
  for(int i=1; i<=q; i++) solve(i);
  
  return 0;
}