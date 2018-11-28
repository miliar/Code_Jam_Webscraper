#include <iostream>
#include <stack>
#include <cstdio>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <iterator>
using namespace std;

#define A first
#define B second

int main()
{
  int i, j, k, l, m, A, N, T, level;
  int motes[100];
  int sum[100];
  int result, adjustment;
  cin >> T;
  for (int t=1; t<=T; ++t)
  {
    level = t;
    cin >> A >> N;
    for (i=0; i<N; ++i)
    {
      cin >> motes[i];
    }
    sort(motes, motes+N);
    sum[0] = 0;
    for (i=1; i<N; ++i)
      sum[i] = sum[i-1]+motes[i-1];
    result = 0;
    adjustment = 0;
    if (A == 1)
    {
      for (i=0; i<N; ++i)
        if (A + sum[i] <= motes[i])
        {
          result = N-i;
          break;
        }
    }
    else
    {
      for (i=0; i<N; ++i)
      {
        if (A > motes[i])
        {
          A += motes[i];
        }
        else
        {
          result = N-i;
          l = 0;
          for (j=i; j<N; ++j)
          {
            adjustment = A;
            while (adjustment <= motes[j])
            {
              adjustment += (adjustment-1);
              ++l;
              // if (t == 8)
                // cout << A << " " << adjustment << " " << l << " \t\t" << j << endl;
            }
            // adjustment = (motes[j] - A)/level*level + level;
            A = adjustment + motes[j];
            for (k=j+1; k<N; ++k)
              if (adjustment > motes[k])
                adjustment += motes[k];
              else
              {
                break;
              }
            // cout << adjustment << " " << k << endl;
            if (l+(N-k) < result)
              result = l+(N-k);
          }
          break;
        }
      }
    }
    printf("Case #%d: %d\n", t, result);
  }
	return 0;
}
