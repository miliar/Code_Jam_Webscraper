#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

void solve()
{
  int n=0;
  int i=0;
  int a[10]={0,0,0,0,0,0,0,0,0,0};
  int cnt=0;
  char c, last='+', s[101];
  cin >> s;

  i=strlen(s);
  c=s[--i];
  while(i>=0)
  {
      if( c!=last)
      {
          cnt++;
          last=c;
      }
      c=s[--i];
  }
  printf("%d\n", cnt);
}

int main(int argc, char *argv[])
{
  int T;
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  scanf("%d", &T);
  forn(t, T)
  {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
