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
using namespace std;

#define SIZE 4

int main(int argc, char* argv[])
{
  freopen(argv[1], "rt", stdin);
  freopen(argv[2], "wt", stdout);

  int T;
  int rid1, rid2;
  int temp;

  set<int> r1;

  cin>>T;
  for (int t=1; t<=T; t++)
  {
    printf("Case #%d: ", t);
    r1.clear();
    cin>>rid1;
    rid1--;
    for (int i = 0; i < SIZE; i++)
    {
      for (int j = 0; j < SIZE; j++)
      {
        cin>>temp;
        if (i == rid1) r1.insert(temp);
      }
    }

    cin>>rid2;
    rid2--;
    int result = 0;
    int count = 0;
    for (int i = 0; i < SIZE; i++)
    {
      for (int j = 0; j < SIZE; j++)
      {
        cin>>temp;
        if (i == rid2 && r1.find(temp) != r1.end())
        {
          count++;
          result = temp;
        }
      }
    }

    if (count == 0)
      printf("Volunteer cheated!\n");
    else if (count == 1)
      printf("%d\n", result);
    else 
      printf("Bad magician!\n");

  }
}
