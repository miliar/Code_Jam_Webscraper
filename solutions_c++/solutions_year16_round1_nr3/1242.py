/*
* Google Code Jam 2016
* Round 1A - Problem 3 - NAME
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
#define SGN(x)              (((x) == 0) ? 0 : ((x) > 0 ? 1 : -1))
#define SZ(a)               ((a).size())
#define FORN(_i, _n)        for (int (_i) = 0; (_i) < (_n); ++(_i))
#define FOR_(_i, _a, _b)    for (int (_i) = (_a); (_i) <= (_b); ++(_i))
#define ALL(stl)            (stl).begin(), (stl).end()
#define INF                 1000000000

using namespace std;


#define OFFICIAL 1

#if OFFICIAL
#define INPUT_FILE    "C-small-attempt2.in"
#define OUTPUT_FILE   "C-small-attempt2.out"
#else
#define INPUT_FILE    "input.txt"
#define OUTPUT_FILE   "output.txt"
#endif

int N;
vector<int> BFF;

void PreGen()
{
  // stuff which executes only once, before reading the input
}

bool Valid(vector<int>& v, int n)
{
  for (int i = 0; i < n; ++i)
  {
    int prev = (i - 1 + n) % n;
    int next = (i + 1) % n;
    if (BFF[v[i]] != v[prev] && BFF[v[i]] != v[next])
      return false;
  }
  return true;
}

int Solve()
{
  // stuff which is executed for each input
  // expects the output to be printed out

  scanf("%d", &N);
  BFF.resize(N + 1, 0);
  for (int i = 1; i <= N; ++i)
    scanf("%d", &BFF[i]);

  vector<int> perm;
  for (int i = 1; i <= N; ++i)
  {
    perm.push_back(i);
  }

  int max = 0;
  vector<int> Sol;
  int iter = 0;
  do
  {
    for (int len = N; len >= 1; --len)
    {
      iter++;
      if (Valid(perm, len) && len > max)
      {
        max = len;
        Sol = perm;
      }
    }
  } while (std::next_permutation(ALL(perm)));
  /*printf("%d iterations\n", iter);
  for (int i = 0; i < max; ++i)
    printf("%d ", Sol[i]);
  printf("\n");*/
  printf("%d", max);

  return 0;
}

int main()
{
  freopen(INPUT_FILE, "rt", stdin);

#if OFFICIAL
  freopen(OUTPUT_FILE, "wt", stdout);
#endif

  PreGen();

  int T, nt;

  scanf("%d\n", &T);

  for (nt = 1; nt <= T; ++nt)
  {
    printf("Case #%d: ", nt);

    if (Solve())
    {
    }

    printf("\n");
  }

  return 0;
}