#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iomanip>
#include <queue>

using namespace std;

int main()
{
  int n;
  cin >> n;
  for(int i = 1; i <= n; i++)
  {
    //solving
    long long len,levels,spots;
    cin >> len >> levels >> spots;
    vector<long long> nums(spots,0);
    if((len-1)/levels + 1 > spots)
    {
      cout << "Case #" << i << ": IMPOSSIBLE" << endl;
      continue;
    }
    int s = 0;
    cout << "Case #" << i << ": ";
    for(auto num : nums)
    {
      for(int j = 0; j < levels; j++)
      {
        num *= len;
        num += s;
        s++;
        if(s >= len) break;
      }
      cout << num+1 << " ";
      if(s >= len) break;
    }
    cout << endl;


    //output
  }
  return 0;
}
