#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <numeric>
#include <complex>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <climits>
using namespace std;

typedef long long ll;
const double EPS = 1e-9;
const int INF = INT_MAX / 4;
typedef vector<int> vint;
typedef pair<int, int> pint;
typedef vector<vector<int> > mat;

#define rep(i, n) REP(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define MSG(a) cout << #a << " " << a << endl;
#define REP(i, x, n) for(int i = x; i < n; i++)
#define pb push_back
#define mp make_pair

int main() {
  int T;
  cin >> T;
  for (int casen = 1; casen <= T; casen++) {
    int x, r, c;
    string ans;
    cin >> x >> r >> c;
    int ma = max(r,c);
    int mi = min(r,c);
    r = mi; c = ma;
    if (x == 1) {
      ans = "GABRIEL";
    } else if (x == 2) {
      if (r % 2 && c % 2) {
        ans = "RICHARD";
      } else {
        ans = "GABRIEL";
      }
    } else if (x == 3) {
      if ((r==2&&c==3)||(r==3&&c==3)||(r==3&&c==4)) ans = "GABRIEL";
      else ans = "RICHARD";
    } else {
      if ((r==3&&c==4)||(r==4&&c==4)) ans = "GABRIEL";
      else ans = "RICHARD";
    }
    printf("Case #%d: %s\n", casen, ans.c_str());
  }
  return 0;
}
