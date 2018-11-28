#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <string>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; ++tt)
  {
    int smax;
    string sline;
    cin >> smax >> sline;
    
    int nFriends = 0;
    int standing = sline[0] - '0';
    for (int ii = 1; ii <= smax; ++ii)
    {
      int diff = max(0, ii - standing);
      nFriends += diff;
      standing += (sline[ii] - '0');
      standing += diff;
    }
    cout << "Case #"  << tt << ": " << nFriends << endl;
  }
  return 0;
}
