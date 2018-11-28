#include "stdafx.h"

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>
#include <set>

using namespace std;

std::set<__int64> primes;

bool isprime(__int64 n)
{
  for (__int64 i = 2; i * i <= n; ++i)
  {
    if (n % i == 0)
      return false;
  }
  return true;
}

__int64 divisor(__int64 n)
{
  for (__int64 i = 2; i * i <= n; ++i)
  {
    if (n % i == 0)
      return i;
  }
  return 1;
}

void precalc(__int64 lb, __int64 ub)
{
  for (__int64 i = lb; i <= ub; ++i)
  {
    if (isprime(i))
      primes.insert(i);
  }
}


__int64 num2dec(std::vector<int>& b, int base)
{
  __int64 res = 0;
  for (int i = 0; i < b.size() ; ++i)
  {
    res = (res * base) + b[i];
  }

  return res;
}

bool nextV(std::vector<int>& v)
{
  int n = v.size();
  int i = n - 2;
  while (i > 0 && v[i] == 1)
    i--;
  if (i > 0)
  {
    v[i] = 1;
    for (int j = i + 1; j < n - 1; ++j)
      v[j] = 0;

    return true;
  }
  return false;
}

void testcase(int i)
{
  int N, J;
  cin >> N >> J;

  std::cout << "Case #" << i << ":" << std::endl;

  int cJ = 0;
  std::vector<int> n(N, 0);
  n[0] = 1;
  n[N - 1] = 1;

  int div[11];

  bool hasNext = true;

  while (cJ < J && hasNext)
  {
    bool prime = false;
    for (int i = 2; i <= 10 && !prime; ++i)
    {
      __int64 num = num2dec(n, i);
      __int64 d = divisor(num);
      if ( d == 1 )
      {
        prime = true;
      }
      else
      {
        div[i] = d;
      }
    }

    if (!prime)
    {
      cJ++;
      for (auto i : n)
        cout << i;

      for (int i = 2; i <= 10 && !prime; ++i)
      {
        cout << " " << div[i];
      }

      __int64 num10 = num2dec(n, 10);
      __int64 div10 = divisor(num10);
      cout << std::endl;
    }

    hasNext = nextV(n);

  }
} 

int main()
{
  //precalc(0, 65536);
  //cout << "nr of primes " << primes.size();
  int n;
	std::cin >> n;
	
	for (int i = 1; i <= n; i++)
	{
		testcase(i);
	}
	
	return 0;
}