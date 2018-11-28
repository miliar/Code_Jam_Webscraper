// Tapan Sahni
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <iomanip>
#include <map>
#include <complex>
#include <set>

using namespace std;
typedef long long LL;
typedef pair <int, int> PII;

const int N = 1e5 + 10;
const LL mod = 1000000007;

void solve() {
  int t, tNum = 1; 
  cin >> t;
  while(t--) {
    int K, C, S;
    cin >> K >> C >> S;
    cout << "Case #" << tNum << ": ";
    for(int i = 1; i <= S; i++)
      cout << i << " ";
    cout << "\n";
    tNum++;
  }
  return; 
}
int main() {
    ios::sync_with_stdio(false) ; cin.tie(nullptr);
    solve();
    return  0;
}
// Never Quit
