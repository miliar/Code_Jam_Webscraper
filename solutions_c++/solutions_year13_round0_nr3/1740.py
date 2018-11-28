#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cmath> 
#include <ctime> 
#include <float.h> 

using namespace std; 

#define REP(i, from, to) for (int i = (from); i < (to); ++i) 
#define FOR(i, n) REP(i, 0, (n)) 
#define ALL(x) x.begin(), x.end() 
#define SIZE(x) (int)x.size() 
#define PB push_back 
#define MP make_pair 

typedef long long i64; 
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef vector<string> VS; 
typedef vector<VS> VVS; 
typedef pair<int, int> PII; 

bool isPalindrom(i64 n) {
  VI digits;
  while (n) {
    digits.PB(n % 10);
    n /= 10;
  }

  FOR (i, SIZE(digits))
    if (digits[i] != digits[SIZE(digits) - i - 1])
      return false;
  return true;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  i64 const MAX_VALUE = 1e7 + 100;
  VI cache(MAX_VALUE);
  
  REP (i, 1, MAX_VALUE) {
    cache[i] = cache[i - 1] + (isPalindrom(i) && isPalindrom((i64)i * i));
  }

  int t;
  cin >> t;

  FOR (tt, t) {
    i64 a, b;
    cin >> a >> b;

    i64 x = sqrt(a + 0.0) - 1, y = sqrt(b + 0.0) + 1;
    while (x * x < a) ++x;
    while (y > 0 && y * y > b) --y;

    i64 res = cache[y] - cache[x - 1];
    
    cout << "Case #" << tt + 1 << ": " << res << endl;
  }

  return 0;
}