#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

void solve()
{
  unsigned long long K,C,S, step=1;
  cin >> K >> C >> S;
  if(K>1)
    step = ((unsigned long long)pow(K,C) - 1) / (K-1);
  unsigned long long val = 1;
  while(K--)
  {
    printf(" %llu", val);
    val+=step;
  }
  printf(" \n");
}

int main(int argc, char *argv[])
{
  int T;
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("D-small.out", "w", stdout);
  scanf("%d", &T);
  forn(t, T)
  {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
