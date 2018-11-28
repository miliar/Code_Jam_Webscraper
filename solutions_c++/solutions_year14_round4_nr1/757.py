#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int main()
{
  int Nprob;
  cin >> Nprob;
  string s;
  getline(cin, s);
  for (int np=0; np<Nprob; np++)
  {
    int N, X;
    vector<int> sizes;
    vector<int> usage;
    cin >> N >> X;
    for (int i=0; i<N; i++)
    {
      int tmp;
      cin >> tmp;
      sizes.push_back(tmp);
      usage.push_back(0);
    }
    sort(sizes.begin(),sizes.end());
    int done = 0;
    int num_used = 0;
    for (int i=N-1; !done && i>=0; i--)
    {
      if (!usage[i])
      {
        for (int j=i-1; !done && j>=0; j--)
        {
          if (sizes[i] + sizes[j] <= X && !usage[j])
          {
            usage[i] = 1;
            usage[j] = 1;
            num_used ++;
            break;
          }
        }
        if (!usage[i])
        {
          usage[i] = 1;
          num_used ++;
        }
      }
    }

    cout << "Case #" << np+1 << ": " << num_used << "\n";
  }
}
