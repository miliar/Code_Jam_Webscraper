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

typedef set<int> TRow;
typedef map<int, TRow> TTab;

//----------------------------------------------------------------------------
int
main ()
{
  freopen ("A-small-1.in", "rt", stdin);
  freopen("A-small-1.out", "wt", stdout);

  int result;

  int T;
  GETI(T);
  FOR(TestCase, 1, T)
    {
      result = 0;
      TTab tab1;
      TTab tab2;

      // load data

      int tip1;
      GETI(tip1);

      for (int ri = 1; ri <= 4; ++ri)
	{
	  TRow row;
	  int n;
	  for (int ci = 1; ci <= 3; ++ci)
	    {
	      GETDI(n, ' ');
	      row.insert (n);
	    }
	  GETI(n);
	  row.insert (n);
	  tab1[ri] = row;
	}

      int tip2;
      GETI(tip2);

      for (int ri = 1; ri <= 4; ++ri)
	{
	  TRow row;
	  int n;
	  for (int ci = 1; ci <= 3; ++ci)
	    {
	      GETDI(n, ' ');
	      row.insert (n);
	    }
	  GETI(n);
	  row.insert (n);
	  tab2[ri] = row;
	}

      // algorithm

      TRow row1 = tab1[tip1];
      TRow row2 = tab2[tip2];

      for (set<int>::iterator cit = row1.begin (); cit != row1.end (); ++cit)
	{
	  set<int>::iterator fit = row2.find (*cit);
	  if (fit != row2.end ())
	    {
	      if (result == 0)
		result = *cit;
	      else
		result = -1;
	    }
	}

      if (result == 0)
	cout << "Case #" << TestCase << ": " << "Volunteer cheated!" << endl;
      else if (result == -1)
	cout << "Case #" << TestCase << ": " << "Bad magician!" << endl;
      else
	cout << "Case #" << TestCase << ": " << result << endl;
    }

  return EXIT_SUCCESS;
}

