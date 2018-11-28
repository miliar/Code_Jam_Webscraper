#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <sstream>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <sys/time.h>
#include <iostream>
 
using namespace std;

typedef long long LL;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define MP make_pair
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define PII pair<int, int>
#define PSS pair<string, string>
#define PLL pair<long long, long long>
#define CLEAR(a) memset(a, 0, sizeof(a))
#define prev eruyvuy
#define INF 2000000007
#define next abc
const double EPS = 1E-12;
const LL mod = 1000000007;
 
using namespace std;

int smax;
string s;


int main() {
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  FOR(tt,t) {
    cin >> smax;
    cin >> s;
    int cur = 0;
    int cnt = 0;
    FOR(i, s.length()) {
      if (s[i] == 0)
        continue;
      if (cur >= i) {
        cur += (s[i] - '0');
      } else {
        int need = i - cur;
        cur += (s[i] - '0');
        cur += need;
        cnt += need;
      }
    }
    cout << "Case #" << tt+1 << ": " << cnt << endl;
  }
  return 0;
}
