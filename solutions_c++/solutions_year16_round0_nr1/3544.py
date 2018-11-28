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
    LL cnt1 = 0;
    for(int i = 0; i <= 9; i++)
      cnt1 |= (1 << i);
    LL n; 
    cin >> n;
    LL ans = 0;
    bool f = false;
    for(int j = 1; j <= 100; j++) {
      LL tmp = n * 1LL * j, tmp1 = n * 1LL * j;
      while(tmp > 0) {
        ans = (ans | (1<< (tmp % 10)));
        tmp /= 10;
      }
      if(ans == cnt1) {
        cout << "Case #" << tNum << ": " << tmp1 << endl;
        f = true;
        break;
      }
    }
    if(f == true) {
      tNum++;
      continue;
    }
    cout << "Case #" << tNum << ": " << "INSOMNIA" << endl;
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
