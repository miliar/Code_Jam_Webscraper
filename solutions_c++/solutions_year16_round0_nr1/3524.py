#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

void solve()
{
  int n;
  int i=0;
  int a[10]={0,0,0,0,0,0,0,0,0,0};
  int cnt=0;
  int t;
  cin >> n;
  if(n==0)
  {
      printf("INSOMNIA\n");
      return;
  }
  while(cnt<10)
  {
      i++;
      t=n*i;
      while(t>0)
      {
          if(a[t % 10] == 0)
          {
              a[t % 10] = 1;
              cnt++;
          }
          t /= 10;
      }
  }
  printf("%d\n", n*i);
}

int main(int argc, char *argv[])
{
  int T;
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  scanf("%d", &T);
  forn(t, T)
  {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
