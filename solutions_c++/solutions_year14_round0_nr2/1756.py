/*
 * CookieClicker.C
 *
 *  Created on: Apr 11, 2014
 *      Author: Abhay
 */


#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }


//ifstream fin("C:\\Users\\Abhay\\Eclipse-Indigo-CPP\\HelloWorld\\src\\data.in");
//#define cin fin

static const double initSpeed=2.0;
int main()
{
  int T;
  cin>>T;
  cout.precision(7);
  for(int C=1;C<=T;++C)
  {
    double Cost, FarmAdd, XTarget;
    cin>> Cost >> FarmAdd >> XTarget;
    double TotalTime = 0.0;

    double currSpeed, TimeDirect, TimeUpgrade, SpeedAfterUpgrade, TimeAfterUpgrade, Diff = 0.0;
    currSpeed = initSpeed;
    do
    {
      TimeDirect = XTarget/currSpeed;
      TimeUpgrade = Cost/currSpeed;
      SpeedAfterUpgrade = currSpeed + FarmAdd;
      TimeAfterUpgrade = XTarget/SpeedAfterUpgrade;
      Diff = TimeDirect - (TimeUpgrade + TimeAfterUpgrade);

      if(Diff > 0.0)
      {
        TotalTime += TimeUpgrade;
        currSpeed = SpeedAfterUpgrade;
      }
      else
      {
        TotalTime += TimeDirect;
        break;
      }
    }while(1);
    printf("Case #%d: %.7f\n",C,TotalTime);
  }
  return 0;
}





