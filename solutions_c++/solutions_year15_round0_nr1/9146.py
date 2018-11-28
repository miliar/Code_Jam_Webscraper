#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <tuple>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <unordered_map>
#include <random>

using namespace std;

int NumPeopleToInvite(int maxS, string shyness) {

  if (shyness.size() != maxS+1) throw length_error("bad input");

  vector<int> standingVec(maxS+1, 0);
  int n = 0;

  standingVec[0] = shyness[0] - '0';
  for(int i=1; i<=maxS; ++i) {
    standingVec[i] = shyness[i] - '0';
    int np = standingVec[i];

    if (np > 0 && standingVec[i-1] < i) {
      n += i - standingVec[i-1];
      standingVec[i-1] = i;
    }

    standingVec[i] += standingVec[i-1];
  }

  return n;
}

int main() {
  int T;
  int ncase = 1;

  cin >> T;
  while( T-- ) {
    int maxS;
    string shyness;
    cin >> maxS >> shyness;
    int n = NumPeopleToInvite(maxS, shyness);
    cout << "Case #" << ncase++ << ": " << n << endl; 
  }
}
    
