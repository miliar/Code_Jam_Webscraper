#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
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

//#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif

#pragma GCC diagnostic warning "-Wall"
#define WRITE(x) DEBUG { cout << x << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << x << endl; }
#define ALL(x) (x).begin(), (x).end()
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#include <boost/lexical_cast.hpp>

typedef unsigned long long ull;
const ull MAXN = 1E14;
std::vector<ull> numbers;

bool palindromeq(ull n)
{
  //for (int i = n, j = 1; i != 0; i /= 10, j++);
  //WATCH(j);
  string s = boost::lexical_cast<std::string>(n);
  string r = s;
  reverse(ALL(r));
  return r == s;
}

void precompute()
{
	for (ull n = 0; n*n <= MAXN; ++n) {
	  if (palindromeq(n) and palindromeq(n*n)) {
      //WATCH(n);
      //WATCH(n*n);
      numbers.push_back(n*n);
    }
  }
}

int main(){
  precompute();
	//Descomente para acelerar cin
	//ios::sync_with_stdio(false);
	int ntc; cin >> ntc;
	FORN(tc, 1, ntc+1) {
    ull a = 0, b = 0, sol = 0;
    cin >> a >> b;
    FOREACH(e, numbers) if ( a <= *e and *e <= b ) ++sol;
    cout << "Case #" << tc << ": " << sol << endl;
  }
	
}
