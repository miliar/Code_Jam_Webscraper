#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <cassert>
#include <assert.h>
#include <bitset>
#include <functional>
#include <utility>
#include <iomanip>
#include <cctype>
#include <gmp.h>
#include <gmpxx.h>

using namespace std;

bool comp(pair<int,int> a,pair<int,int> b) {return a.first < b.first; }

typedef long long ll;
typedef unsigned long long ull;

#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(s,i) for ( __typeof((s).begin()) i = ((s).begin())   ; i != (s).end(); ++i)  
#define mp(a,b) make_pair(a,b)

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)

//////////////////////////////////////////////////////////////////////////

int main (int argc, char* argv[]) {

  ifstream in (argv[1]);
  ofstream out ("problem.out");
  string line;
  int nbTests;
  out.precision(12);

  in >> nbTests;
  getline(in, line);
  int lawn[100][100];
  bool rowok[100];
  bool colok[100];
  
  for (int test=0; test<nbTests; test++) {
    FOR(i,0,100) 
      rowok[i] = colok[i] = false;
    int n, m;
    in >> n >> m;
    FOR(i,0,n) {
      FOR(j,0,m) {
	in >> lawn[i][j];
      }
    }

    FOR(h,1,101) { 
      /* rows */
      FOR(i,0,n) {
	if (rowok[i]) 
	  continue;
	bool ok = true;
	FOR(j,0,m) {
	  if (!colok[j] && lawn[i][j] != h)
	    ok = false;
	}
	if (ok)
	  rowok[i] = true;
      }
      /* columns */
      FOR(j,0,m) {
	if (colok[j]) 
	  continue;
	bool ok = true;
	FOR(i,0,n) {
	  if (!rowok[i] && lawn[i][j] != h)
	    ok = false;
	}
	if (ok)
	  colok[j] = true;
      }
    }

    bool ok = true;
    FOR(i,0,n) if (!rowok[i]) ok = false;
    FOR(j,0,m) if (!colok[j]) ok = false;
    
    if (ok)
      out << "Case #" << test+1 << ": YES" << endl;
    else
      out << "Case #" << test+1 << ": NO" << endl;
  }
}

