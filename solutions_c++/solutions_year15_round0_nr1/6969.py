#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <map>
#include <queue>
#include <climits>
#include <algorithm>
#include <cmath>
using namespace std;
#define FOR(i,N) for (int i = 0; i < N; i++)

int main()
{
  int T;
  cin >> T;
  FOR(i,T)
    {
      int SMax, total = 0, add = 0;
      char dig;
      cin >> SMax;
      FOR(k,SMax+1)
        {
          cin >> dig;
          int d_dig = dig - '0';
          if (total < k)
            {
              add += (k-total);
              total = k;
            }
          total += d_dig;
        }
      cout << "Case #" << i+1 << ": " << add << endl;
      //cout << sol << endl;
    }
  return 0;
}
