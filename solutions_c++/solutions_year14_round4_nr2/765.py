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
    int N;
    cin >> N;
    vector<int> nums;
    int max = -1;
    int max_index = -1;
    for (int i=0; i<N; i++)
    {
      int tmp;
      cin >> tmp;
      if (tmp > max)
      {
        max = tmp;
        max_index = i;
      }
      nums.push_back(tmp);
    }
    int num_steps = 0;
    int good_start = -1;
    int good_stop  = N;
    while (good_stop - good_start > 3)
    {
      int min = 1000000001;
      int min_index = -1;
      for (int i=good_start+1; i<good_stop; i++)
      {
        if (nums[i] < min)
        {
          min = nums[i];
          min_index = i;
        }
      }
      if (good_stop-min_index < min_index-good_start)
      {
        num_steps += good_stop-min_index-1;
        good_stop--;
        for (int i=min_index; i<good_stop; i++)
          nums[i] = nums[i+1];
        nums[good_stop] = min;
      }
      else
      {
        num_steps += min_index-good_start-1;
        good_start++;
        for (int i=min_index; i>good_start; i--)
          nums[i] = nums[i-1];
        nums[good_start] = min;
      }
    }
    cout << "Case #" << np+1 <<": " << num_steps << "\n";
  }
}
