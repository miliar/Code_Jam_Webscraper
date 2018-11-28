/*
 * Google Code Jam 2016
 * Round 1A - Problem 1 - NAME
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
  #define INPUT_FILE    "A-large.in"
  #define OUTPUT_FILE   "A-large.out"
#else
  #define INPUT_FILE    "input.txt"
  #define OUTPUT_FILE   "output.txt"
#endif

string S, Sol;

void PreGen()
{
  // stuff which executes only once, before reading the input
}

void back(string &s, int len)
{
  if (len == S.size())
  {
    if (s > Sol || Sol.size() == 0)
    {
      Sol = s;
    }
  }
  else
  {
    char nextLetter = S[len];

    string os = s;
    s = os + nextLetter;
    back(s, len + 1);
    s = nextLetter + os;
    back(s, len + 1);
  }
}

int Solve()
{
  // stuff which is executed for each input
  // expects the output to be printed out

  char s[1024];
  scanf("%s\n", &s);

  Sol.clear();
  S = s;

  /*string os;
  os.push_back(S[0]);
  back(os, 1);

  printf("\n%s\n", Sol.c_str());


  Sol.clear();*/
  Sol.push_back(S[0]);
  
  for (int i = 1; i < S.size(); ++i)
  {
    if (S[i] >= Sol[0])
      Sol = S[i] + Sol;
    else
      Sol.push_back(S[i]);
  }
  printf("%s", Sol.c_str());

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