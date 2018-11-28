#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <assert.h>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair

using namespace std;

bool solve2 (long long p, long long n, long long x)
{
  if (p<=0)
    return 0;
  if (p>=(1ll<<n))
    return 1;
  if (x==(1ll<<n)-1)
    return 0;
  return solve2(p,n-1,(x+1)/2);
}

bool solve1 (long long p, long long n, long long x)
{
  if (p<=0)
    return 0;
  if (p>=(1ll<<n) || x==0)
    return 1;
  return solve1(p-(1ll<<(n-1)),n-1,(x-1)/2);
}

int main()
{
  int tst, cnt;
  long long l, r, tmp, p, n;
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    printf("Case #%d: ", cnt);
    cin>>n>>p;
    l=0, r=(1ll<<n);
    while (r-l>1)
      (solve1(p,n,(l+r)/2))?(l=(l+r)/2):(r=(l+r)/2);
    tmp=l;
    l=0, r=(1ll<<n);
    while (r-l>1)
      (solve2(p,n,(l+r)/2))?(l=(l+r)/2):(r=(l+r)/2);
    cout<<tmp<<" "<<l<<endl;
  }
  return 0;
}
