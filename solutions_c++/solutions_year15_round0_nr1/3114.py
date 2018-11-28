#include <cstring>
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
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define REP(i, a, b) for(int i = (a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i > (b); --i)
#define REPD(i, a, b) for(int i = (a); i >=(b); --i)
#define TR(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#define RESET(a, v) memset(a, (v), sizeof(a))
#define SZ(a) (int(a.size()))
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair
#define LL long long
#define LD long double
#define II pair<int, int>
#define X first
#define Y second
#define VI vector<int>
#define VII vector<II>
#define endl '\n'

using namespace std;

int nTest, n;

int main() {
  ios::sync_with_stdio(0); cin.tie(0);
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  cin >> nTest;
  REP(test, 1, nTest) {
    cin >> n;
    int sum = 0, ans = 0;
    char c;
    REP(i, 0, n) {
      cin >> c;
      if (i && sum < i) {
        ans += i - sum;
        sum = i;
      }
      sum += c - '0';
    }
    cout << "Case #" << test << ": " << ans << endl;
  }
  return 0;
}
