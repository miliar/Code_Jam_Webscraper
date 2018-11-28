#define NOMINMAX
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
using std::min;
using std::max;

int main(void)
{
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; ++i)
  {
    string s;
    int max;
    cin >> max >> s;
    int sum = 0;
    vector<int> scan;
    for (char c : s)
    {
      int cur = (int) c - '0';
      sum += cur;
      scan.push_back(sum);
    }

    int added = 0;
    for (int j = 1; j < s.length(); ++j)
    {
      if (j > (scan[j-1] + added))
      {
        // cout << j << " > " << scan[j-1] << " + " << added << "\n";
        added += 1;
      }
    }

    cout << "Case #" << i+1 << ": " << added << "\n";
  }
}