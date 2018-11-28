/*
 * Google Code Jam 2013
 * Qualification Round - Problem C - Fair and Square
 */

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <iostream>
#include <sstream>
#include <functional>
#include <deque>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define MIN(a, b)           ((a) > (b) ? (b) : (a))
#define MAX(a, b)           ((a) > (b) ? (a) : (b))
#define ABS(x)              ((x) > 0 ? (x) : -(x))
#define FORN(_i, _n)        for ((_i) = 0; (_i) < (_n); ++(_i))

using namespace std;


#define OFFICIAL 1

#if OFFICIAL
  #define INPUT_FILE    "C-large-1.in"
  #define OUTPUT_FILE   "C-large-1.out"
#else
  #define INPUT_FILE    "input.txt"
#endif

#define MIN(a, b)       ((a) > (b) ? (b) : (a))
#define MAX(a, b)       ((a) > (b) ? (a) : (b))
#define ABS(a)          ((a) > 0 ? (a) : -(a))

set<long long> S;

long long All1014[39] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321,
                       4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521,
                       400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 
                       40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201,
                       1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121,
                       1232346432321, 1234567654321, 4000008000004, 4004009004004};

bool Palindrome(long long n)
{
  char sz[100];

  _i64toa(n, sz, 10);
  int len = strlen(sz);
  for (int i = 0; 2 * i < len; ++i)
    if (sz[i] != sz[len - i - 1])
    {
      return false;
    }
  return true;
}

bool FairAndSquare(long long n)
{
  long long sq = sqrtl(n);

  if (sq * sq != n)
  {
    return false;
  }
  
  return Palindrome(sq) && Palindrome(n);
}

void Solve()
{
  long long a, b;

  scanf("%lld %lld", &a, &b);

  S.clear();
  int count = 0;
  /*
  // odd palindromes
  for (long long i = 1; i <= 10000000; ++i)
  {
    // create a palindrome with first digits i, and the rest i in mirror except the middle
    long long n = i, nr = i;

    n /= 10;
    while (n > 0)
    {
      nr = nr * 10 + n % 10;
      n /= 10;
    }

    if (FairAndSquare(nr))
    {
      S.insert(nr);
    }
  }*/

  for (int i = 0; i < 39; ++i)
  {
    if (All1014[i] < a)
    {
      continue;
    }
    if (All1014[i] > b)
    {
      break;
    }
    ++count;
  }
  printf("%d", count);
  return;
}

int main()
{
  freopen(INPUT_FILE, "rt", stdin);

#if OFFICIAL
  freopen(OUTPUT_FILE, "wt", stdout);
#endif

  int T, nt;

  scanf("%d\n", &T);

  for (nt = 1; nt <= T; ++nt)
  {
    printf("Case #%d: ", nt);

    Solve();

    printf("\n");
  }

  return 0;
}