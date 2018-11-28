#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iterator>
#define FOR(i,a,n) for(int i = (a); i < (int)(n); ++i)
#define foreach(itr,c) for(decltype((c).begin()) itr=(c).begin(); itr != (c).end(); itr++)
#define MP(a,b) make_pair(a,b)

using namespace std;

//typedef __int64 ll;
//typedef unsigned __int64 ull;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;

ll n, xx;
int m, mk[100];
void solve() {
  ll x = n, y;
  while(x) {
    y = x % 10;
    if(mk[y] == 0) {
      ++m;
      mk[y] = 1;
    }
    x /= 10;
  }
}
int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int t;
  cin >> t;
  FOR(tt, 1, t + 1) {
    cin >> n;
    xx = n;
    printf("Case #%d: ", tt);
    if(n == 0) {
      puts("INSOMNIA");
      continue;
    }
    memset(mk, 0, sizeof(mk));
    m = 0;
    while(1) {
      solve();
      if(m == 10) break;
      n += xx;
    }
    cout << n << endl;
  }
}
