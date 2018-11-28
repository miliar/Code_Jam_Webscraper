#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define GETS(s) getline(cin, s);
#define GETDS(s, d) getline(cin, s, d);
#define GETI(i) { string _s; getline(cin, _s); stringstream _ss; _ss << _s; _ss >> i; }
#define GETDI(i, d) { string _s; getline(cin, _s, d); stringstream _ss; _ss << _s; _ss >> i; }
#define GETF(f) { string _s; getline(cin, _s); f = atof(_s.c_str()); }
#define GETDF(f, d) { string _s; getline(cin, _s, d); f = atof(_s.c_str()); }

//----------------------------------------------------------------------------
int
main ()
{
  freopen ("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);

  cout.setf (std::ios::fixed, std::ios::floatfield);
  cout.precision (7);

  double result;

  int T;
  GETI(T);
  FOR(TestCase, 1, T)
    {
      result = 0;

      // load data

      double C, F, X;
      GETDF(C, ' ');
      GETDF(F, ' ');
      GETF(X);

      // algorithm

      if (X > C)
	{
	  double t = 0;
	  int n = 0;
	  double xc = X - C;
	  double f2 = 2 / F;
	  while (n < 100000)
	    {
	      if (xc / (f2 + n) < C)
		break;
	      else
		++n;
	    }
	  //cout << "n=" << n << " ";

	  for (int i = 0; i < n; ++i)
	    {
	      t += C / (2 + i * F);
	    }
	  t += X / (2 + n * F);

	  result = t;
	}
      else
	result = X / 2;

      cout << "Case #" << TestCase << ": " << result << endl;
    }

  return EXIT_SUCCESS;
}

