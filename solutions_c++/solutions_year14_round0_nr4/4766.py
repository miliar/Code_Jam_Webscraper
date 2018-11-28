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

int i, j, k, N, T;
double blocks[2][1000];

int main()
{
  cin >> T;
  for (int t=1; t<=T; ++t)
  {
    cin >> N;
    for (i=0; i<2; ++i)
      for (j=0; j<N; ++j)
        cin >> blocks[i][j];

    sort(blocks[0], blocks[0]+N);
    sort(blocks[1], blocks[1]+N);
    int result1 = 0, result2 = 0;
    double block;
    j = 0;
    k = N-1;
    for (i=0; i<N; ++i)
    {
      block = blocks[0][i];
      if (block > blocks[1][j])
      {
        ++j;
        ++result1;
      }
    }
    i = j = 0;
    while (i < N && j < N)
    {
      block = blocks[0][i];
      while (j < N && blocks[1][j] < block) ++j;
      if (j >= N)
        break;
//      else
//        cout << block << " " << blocks[1][j] << endl;
      ++i;
      ++j;
    }
    result2 = N-i;
    cout << "Case #" << t << ": " << result1 << " " << result2 << endl;
  }
	return 0;
}
