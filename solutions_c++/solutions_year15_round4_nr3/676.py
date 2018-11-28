#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>
#include <unordered_map>

typedef unsigned int uint32;
typedef signed long long int64;
typedef unsigned long long uint64;

using namespace std;

#define ALL(a) a.begin(), a.end()
#define FOR(a) for (int i = 0; i < (a); ++i)
#define D(a) #a << ": " << a << "\n"

map<string, int> convertor;
int id;

int main()
{
  int CASES;
  cin >> CASES;
  for (int CASE = 1; CASE <= CASES; ++CASE)
  {
    int n;
    cin >> n;
    vector<vector<int>> arr(n);
    convertor.clear();
    id = 1;
    FOR(n)
    {
      char c = 0;
      while (c != '\n')
      {
        string in;
        cin >> in;
        int& iid = convertor[in];
        if (!iid)
          iid = id++;

        arr[i].push_back(iid);
        scanf("%c", &c);
      }
    }

    int limit = 1<<(n-2);
    uint32 res = 1000000;

    vector<unsigned char> base(id);
    for (int i = 0; i < 2; ++i)
    {
      int flag = 0x1;
      if (i == 1)
        flag = 0x2;

      for (uint32 j = 0; j < arr[i].size(); ++j)
        base[arr[i][j]] |= flag;
    }


    for (int mask = 0; mask < limit; ++mask)
    {
      vector<unsigned char> m = base;
      for (int i = 2; i < n; ++i)
      {
        int flag = 0x1;
        if (mask & (1<<(i-2)))
          flag = 0x2;

        for (uint32 j = 0; j < arr[i].size(); ++j)
          m[arr[i][j]] |= flag;
      }

      uint32 r = 0;
      for (int i = 1; i < id; ++i)
        if (m[i] == 0x3)
          ++r;

      res = min(res, r);
    }

    printf("Case #%d: %d\n", CASE, res);
  }

  return 0;
}
