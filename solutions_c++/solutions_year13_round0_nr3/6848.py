#include <iostream>
#include <stdio.h>
#include <cmath>
#include <limits.h>
#include <iomanip>
#include <queue>
#include <cstring>
#include <stdlib.h>
#include <sstream>
#include <algorithm>
#include <stack>


using namespace std;

#define FOR(i, v, x) for (int i = v; i < x; i++)
#define RPT(i, x) for (long long int i = 0; i < x; i++)
#define RPT1(i, x) for (int i = 1; i <= x; i++)
#define RPTD(i, x) for (int i = x; i > 0; i--)
#define RPTD0(i, x) for (int i = x; i >= 0; i--)

#define EPS 1.0E-5

#define MOD 1000000007
#define lli long long int

using namespace std;

string toString (lli what)
  {
     ostringstream ss;
     ss << what;
     return ss.str();
  }

bool checkPal(lli what)
{
 string foo = toString(what);
 int len = foo.length();
 if(len < 2) return true;

 RPT(i, len/2){if(foo[i]!=foo[len-i-1])return false;}
 return true;
}

int main()
{

 int cnt;
 cin >> cnt;

 RPT(i, cnt)
 {
  int x, y, sqx, sqy;
  cin >> x >> y;

  sqx = sqrt(x) - 1;
  if(sqx < 1) sqx = 1;

  sqy = sqrt(y) + 1;

  int res = 0;

  for(lli j = sqx; j <= sqy; j++)
  {
   lli foo = j;
   if(!checkPal(foo)) continue;
   foo *= foo;
   if(foo < x) continue;
   if(foo > y) break;

   if(checkPal(foo)) {res++;}
  }

  cout << "Case #" << i+1 << ": " << res << endl;

 }

}

