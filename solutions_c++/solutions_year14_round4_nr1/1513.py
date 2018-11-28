#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <utility>
#include <list>
#include <cmath>
#include <set>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    int N, X;
    vector<int> files;
    cin >> N >> X;
    copy_n(istream_iterator<int>(cin), N, back_inserter(files));
    cout << "Case #" << i << ": ";
    sort(files.begin(), files.end(), greater<int>());
    int D = 0;
    while (!files.empty())
    {
      int S = files.front();
      files.erase(files.begin());
      auto it = lower_bound(files.begin(), files.end(), X-S, greater<int>());
      if (it != files.end())
	files.erase(it);
      ++D;
    }
    cout << D << endl;
  }
  return 0;
}
