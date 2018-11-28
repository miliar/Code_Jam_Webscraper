#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

long long bin2base(int num, int b)
{
    long long v, m;
    if(b==2)
        return num;
    v=0;
    m=1;
    while( num>0)
    {
        if(num%2)
            v+=m;
        num/=2;
        m*=b;
    }
  return v;
}

void solve()
{
  int N,J;
  int maxnum, num=1, b, j;
  char s[4000];
  printf("\n", s);
  cin >> N >> J;

  num += (int)pow(2,N-1);
  maxnum = (int)pow(2,N);
  while(num<maxnum && J>0)
  {
      sprintf( s, "%lld", bin2base(num,10));
      int cnt = 1;
      for(b=2;b<=10;b++)
      {
          long long val=bin2base(num,b);
          for( j=2;j<300;j++)
          {
             if(val%j == 0)
             {
                 cnt++;
                 sprintf(s, "%s %d", s, j);
                 break;
             }
          }
          if(cnt<b)
          {
            // divisor not found, try next
            break;
          }
      }
      if(cnt==10)
      {
          printf("%s\n", s);
          J--;
      }
      num+=2;
  }
  if( J>0)
      printf("FAILURE\n");
}

int main(int argc, char *argv[])
{
  int T;
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small.out", "w", stdout);
  scanf("%d", &T);
  forn(t, T)
  {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
