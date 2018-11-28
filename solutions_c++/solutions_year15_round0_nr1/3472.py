#include <cstdio>

void solve(int test)
{
  char t[1005];
  int n;
  
  scanf("%d", &n);
  scanf("%s", t);
  
  int wynik=0, ile=0;
  for(int i=0; i<=n; i++)
  {
    while(ile<i) wynik++, ile++;
    ile+=t[i]-'0';
  }
  
  printf("Case #%d: %d\n", test, wynik);
  
  //for(int i=0; i<=n; i++) printf("%c", t[i]);
  //printf("\n");
}

int main()
{
  int q;
  scanf("%d", &q);

  for(int i=1; i<=q; i++) solve(i);
  
  return 0;
}