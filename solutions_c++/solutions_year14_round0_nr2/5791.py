#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <cassert>
#include <iomanip>
using namespace std;

typedef long long ll;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
bool ISINT(double x){return fabs(x-(int)round(x))<EPS;}
bool ISEQ(double x,double y){return fabs(x-y)<EPS;}
string itos(ll x){stringstream ss;ss<<x;return ss.str();}
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define EREP(i,a,b) for(int i=a;i<=b;i++)
#define erep(i,n) EREP(i,0,n)
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin();itr!=c.end();itr++)

int main(void){
  int T;
  cin >> T;

  for(int CASE = 1; CASE <= T; CASE++){
    cout << "Case #" << CASE << ": ";

    double C, F, X;
    cin >> C >> F >> X;

    double ans = X / 2.0;
    double sp = 2;
    double tm = 0;

    for(int farm = 0; farm <= (int)(X + 1); farm++){
      double tm_buy = C / sp;

      tm += tm_buy;
      sp += F;
      ans = min(ans, tm + X / sp);
    }

    cout << setprecision(7) << fixed << ans << endl;
  }
}
