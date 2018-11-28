#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define rep(x,n) for(int x = 0; x < n; ++x)
#define print(x) cout << x << endl
#define dbg(x) cerr << #x << " == " << x << endl
#define _ << " , " <<
#define mp make_pair
#define x first
#define y second

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;
typedef pair<int,int> pii;

const int maxn =  1111;
int smax;
char value[maxn];

void read() {
  cin >> smax >> value;
}

void process(int testcase) {
  int x = 0, at = 0;
  rep(i,smax+1) {
    x = max(x, i - at);
    at += value[i] - '0';
  }
  printf("Case #%d: %d\n", testcase, x);
}

int main() {
  int T;
  cin >> T;
  for(int testcase=1;testcase<=T;testcase++) {
    read();
    process(testcase);
  }
  return 0;
}

