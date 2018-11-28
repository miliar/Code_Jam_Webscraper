#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

typedef vector<int> vi;

vi a, b;
int n;

void init()
{
  cin>>n;
  a = vi(n); b = vi(n);
  for(int i = 0; i < n; i++) cin>>a[i];
  for(int i = 0; i < n; i++) cin>>b[i];
}

bool check(vi v)
{
  vi aa = vi(n);
  vi bb = vi(n);
  aa[0] = 1;
  for(int i = 1; i < n; i++)
  {
    int Max = 1;
    for(int j = 0; j < i; j++)
    {
      if(v[j] < v[i]) Max = max(Max, aa[j] + 1);
    }
    aa[i] = Max;
  }
  bb[n - 1] = 1;
  for(int i = n - 2; i >= 0; i--)
  {
    int Max = 1;
    for(int j = i + 1; j < n; j++)
    {
      if(v[j] < v[i]) Max = max(Max, bb[j] + 1);
    }
    bb[i] = Max;
  }
  for(int i = 0; i < n; i++)
  {
    if(aa[i] != a[i] || bb[i] != b[i])
    {
      /*printf("error!\nReq:\n");
      for(int j = 0; j < n; j++) printf("%d ", a[j]); printf("\n");
      for(int j = 0; j < n; j++) printf("%d ", b[j]); printf("\n");
      printf("Get:\n");
      for(int j = 0; j < n; j++) printf("%d ", aa[j]); printf("\n");
      for(int j = 0; j < n; j++) printf("%d ", bb[j]); printf("\n");*/
      return 0;
    }
  }
  return 1;
}

#define pb push_back

bool dfs(int pos, vi &res, vi aa, vi bb)
{
  if(pos == n)
  {
    if(check(res)) return 1;
    return 0;
  }
  vi p; int Min = 1 << 29;
  for(int i = 0; i < n; i++)
  {
    if(res[i] != -1) continue;
    int tmp = a[i] + b[i];
    if(tmp < Min) Min = tmp, p.pb(i);
    else if(tmp == Min) p.pb(i);
  }
  for(int i = 0; i < p.size(); i++)
  {
    int pp = p[i];    
    int Max1 = 1;
    for(int j = 0; j < i; j++)
    {
      if(res[i] != -1) Max1 = max(Max1, aa[i] + 1);
    }
    if (Max1 != a[pp]) continue;
    int Max2 = 1;
    for(int j = n - 1; j > i; j--)
    {
      if(res[i] != -1) Max2 = max(Max2, bb[i] + 1);
    }
    if (Max2 != b[pp]) continue;
    res[pp] = pos + 1;
    aa[pp] = Max1;
    bb[pp] = Max2;
    if(dfs(pos + 1, res, aa, bb)) return 1;
    res[pp] = -1;
    aa[pp] = 0, bb[pp] = 0;
  }
  return 0;
}

void out(vi r, int tcase)
{
  printf("Case #%d:", tcase);
  for(int i = 0; i < n; i++)
  {
    printf(" %d", r[i]);
  }
  printf("\n");
}

int main()
{
  int T;
  cin>>T;
  for(int i = 1; i <= T; i++)
  {
    init();
    vi res = vi(n, -1);
    dfs(0, res, vi(n, 0), vi(n, 0));
    out(res, i);
  }
}