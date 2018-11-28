#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

#define MAXN 10000000

using namespace std;

long long a, b; 
int t, l;
char buf[100];
bool isB[MAXN+1];
int sum[MAXN+1];

bool ispal(long long v)
{
  sprintf(buf, "%lld", v);
  l = strlen(buf);
  for (int i = 0; i < l/2; i++)
    if (buf[i] != buf[l-i-1])
      return false;
  return true;
}

int main()
{
  sum[0] = 0;
  isB[0] = true;
  for (int i = 1; i <= MAXN; i++)
    if (ispal(i) && ispal((long long)i * i))
      isB[i] = true, sum[i] = sum[i-1]+1;
    else isB[i] = false, sum[i] = sum[i-1];
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
  {
    scanf("%lld %lld", &a, &b);
    long long lo = max(1, (int)sqrt((long double)a)-3);
    long long hi = (int)sqrt((long double)b)+3;
    int res = 0;
    while (lo * lo < a) lo++;
    while (hi * hi > b) hi--;
    if (lo <= hi)
    {
      res = sum[hi] - sum[lo-1];
    } 
    printf("Case #%d: %d\n", i+1, res);
  }
  return 0;
}
