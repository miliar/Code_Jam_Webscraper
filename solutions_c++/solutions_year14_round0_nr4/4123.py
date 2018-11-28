#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <iomanip>
using namespace std;

int main(int argc, char* argv[])
{
  freopen(argv[1], "rt", stdin);
  freopen(argv[2], "wt", stdout);

  int T;
  int N;

  cin>>T;
  for (int t=1; t<=T; t++)
  {
    printf("Case #%d: ", t);
    cin>>N;
    vector<double> na(N, 0);
    vector<double> ke(N, 0);
    for (int i = 0; i < N; i++)
      cin>>na[i];

    for (int i = 0; i < N; i++)
      cin>>ke[i];

    sort(na.begin(), na.end());
    sort(ke.begin(), ke.end());

    int countD = 0;
    int idx1 = 0, idx2right = N - 1, idx2left = 0;
    while(idx1 < N)
    {
      if (na[idx1] > ke[idx2left])
      {
        countD++;
        idx2left++;
      }
      else if (na[idx1] < ke[idx2right])
      {
        idx2right--;
      }      

      idx1++;
      
    }

    int countW = 0;
    idx1 = N - 1;
    idx2left = 0;idx2right = N - 1;
    while(idx1 >= 0)
    {
      if (na[idx1] > ke[idx2right])
      {
        countW++;
        idx2left++;
      }
      else
      {
        idx2right--;
      }
      idx1--;
    }

    printf("%d %d\n", countD, countW);
  }
}
