#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define forab(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
// need declare it for vc, vc can not use <typeof> keyword
#define foreach(it,c) for(it = c.begin(); it != c.end(); ++it)

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define zero(a) memset(a, 0, sizeof(a))

#define pb push_back
#define mp make_pair

int t;
#define N 102
int number[N];

vector<LL> fire_and_square; 

bool is_palindrome(LL x) {
  int i = 0;
  while (x > 0) {
    number[i] = x % 10;
    i++;
    x /= 10;
  }
  int n = i;

  for (int i = 0; i < n / 2; i++) {
    if (number[i] != number[n - i - 1])
      return false;
  }
  return true;
}

void solve(LL a, LL b) {
  LL aa = (LL)sqrt(1.0 * a);
  LL bb = (LL)sqrt(1.0 * b);
  if (aa * aa < a)
    ++aa;
  LL x = aa;
  for (; x <= bb; ++x) {
    if (is_palindrome(x) && is_palindrome(x * x)) {
      //cout << x * x << endl;
      fire_and_square.push_back(x * x);
    }
  }
}

int main() {
  //freopen("1.in", "r", stdin);
  //freopen("1.out", "w", stdout);

  //freopen("C-small-attempt0.in", "r", stdin);
  //freopen("C-small-attempt0.out", "w", stdout);

  freopen("C-large-1.in", "r", stdin);
  freopen("C-large-1.out", "w", stdout);

  cin >> t;

  // init
  solve(1, 100000000000000);
  for (int cc = 1; cc <= t; cc++) {
    LL a, b;
    LL cnt = 0;
    cin >> a >> b;
    forn(i, fire_and_square.size()) {
      if (fire_and_square[i] >= a && fire_and_square[i] <= b)
        cnt++;
    }
    cout << "Case #" << cc << ": " << cnt << endl;
  }
  return 0;
}
