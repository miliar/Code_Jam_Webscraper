#include <iostream>
#include <algorithm>
#include <cstdio>
#include <set>

typedef unsigned int uint;
typedef long double real;

void merge(real* N, real* K, size_t size, real* R, char* RN)
{
  size_t posN = 0;
  size_t posK = 0;
  size_t posR = 0;
  while (posN < size && posK < size)
  {
    if (N[posN] < K[posK])
    {
      R[posR] = N[posN];
      RN[posR] = 'N';
      ++posR;
      ++posN;
    }
    else
    {
      R[posR] = K[posK];
      RN[posR] = 'K';
      ++posR;
      ++posK;
    }
  }

  if (posN < size)
  {
    for (size_t i = posR; i < 2 * posR; ++i)
    {
      R[i] = N[posN++];
      RN[i] = 'N';
    }
  }
  if (posK < size)
  {
    for (size_t i = posR; i < 2 * posR; ++i)
    {
      R[i] = K[posK++];
      RN[i] = 'K';
    }
  }
}

uint solve_deceitful_war(real* N, real* K, size_t size)
{
  static real RV[4000];
  static char RN[4000];
  merge(N, K, size, RV, RN);  
  
  uint pre = 0;
  uint dominated = 0;  

  for (size_t i = 0; i < size * 2; ++i)
  {
    if (RN[i] == 'N' && pre > 0)
    {
      --pre;
      ++dominated;
    }

    if (RN[i] == 'K')
    {
      ++pre;
    }
  }
  return dominated;
}

uint solve_war(real* N_, real* K_, size_t size)
{
  std::set<real> N(N_, N_ + size);
  std::set<real> K(K_, K_ + size);
  uint dominated = 0;
  for (size_t r = 0; r < size; ++r)
  {
    real NC = *N.begin();
    real KC = *K.begin();
    auto it = K.upper_bound(NC);
    if (it != K.end())
    {
      KC = *it;
      K.erase(it);
    }
    else
    {
      K.erase(K.begin());
    }
    N.erase(N.begin());

    if (NC > KC) { ++dominated; }
  }
  return dominated;
}

int main()
{
  size_t T = 0;
  scanf("%lu", &T);

  real N[2000]; 
  real K[2000]; 
  for (size_t t = 1; t <= T; ++t)  
  {
    size_t size = 0;
    scanf("%lu", &size);
    for (size_t i = 0; i < size; ++i)
    {
      scanf("%Lf", &N[i]);
    }
    for (size_t i = 0; i < size; ++i)
    {
      scanf("%Lf", &K[i]);
    }
    std::sort(N, N + size);
    std::sort(K, K + size);
    
    printf("Case #%lu: %u %u\n", t, solve_deceitful_war(N, K, size), solve_war(N, K, size));
  }
}


