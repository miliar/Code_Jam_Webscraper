#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long LL;

int j, n;
LL last; 

LL mulmod(LL a, LL b, LL mod)
{
  LL x = 0,y = a % mod;
  while (b > 0)
  {
    if (b % 2 == 1)
    {    
      x = (x + y) % mod;
    }
    y = (y * 2) % mod;
    b /= 2;
  }
  return x % mod;
}

LL modulo(LL base, LL exponent, LL mod)
{
  LL x = 1;
  LL y = base;
  while (exponent > 0)
  {
    if (exponent % 2 == 1)
      x = (x * y) % mod;
    y = (y * y) % mod;
    exponent = exponent / 2;
  }
  return x % mod;
}

bool Miller(LL p,int iteration)
{
  if (p < 2)
  {
    return false;
  }
  if (p != 2 && p % 2==0)
  {
    return false;
  }
  LL s = p - 1;
  while (s % 2 == 0)
  {
    s /= 2;
  }
  LL alist[12] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
  for (int i = 0; i < iteration; i++)
  {
    LL a = alist[i], temp = s;
    LL mod = modulo(a, temp, p);
    while (temp != p - 1 && mod != 1 && mod != p - 1)
    {
      mod = mulmod(mod, mod, p);
      temp *= 2;
    }
    if (mod != p - 1 && temp % 2 == 0)
    {
      return false;
    }
  }
  return true;
}

LL get(LL v)
{
  LL k=-1;
  for(LL j=2; j*j <= v; j++)
  {
    if(v%j == 0)
    {
      k = j;
      break;
    }
  }
  return k;
} 

bool check(LL v, vector<LL>& vec)
{
  for(LL i=2; i<=10; i++)
  {
    LL t = v;
    LL b = 1;
    LL ret = 0;
    while(t > 0)
    {
      if(t&1)
        ret += b;
      t>>=1;
      b *= i;
    }
    b = get(ret);
    if(b == -1)
      return false;
    vec.push_back(b);
  }
  return true;
}

void solve()
{
  vector<LL> rets;
  while(!check(last, rets))
  {
    rets.clear();
    last += 2;
  }

  LL tem = last, ret = 0, b = 1;
  while(tem > 0)
  {
    if(tem&1)
      ret += b;
    tem >>= 1;
    b *= 10;
  }

  printf("%lld ", ret);
  for(int i=0; i<rets.size(); i++)
    printf("%lld%c", rets[i], i == rets.size() - 1? '\n':' ');

  last += 2;
}

int main()
{
  freopen("CSin.txt", "r", stdin);
  freopen("CSout.txt", "w", stdout);

  scanf("%*d");
  scanf("%d %d", &n, &j);
  printf("Case #1:\n");
  last = (1<<(n-1))+1;
  for(int i=0; i<j; i++)
    solve();
  return 0;
}
