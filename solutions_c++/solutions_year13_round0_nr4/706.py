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

typedef vector<int> vi; 
typedef vector<vi> vvi; 

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)

#define NBTYPE 401
#define NBCHEST 201

int main (int argc, char* argv[]) {

  ifstream in (argv[1]);
  ofstream out ("problem.out");
  string line;
  int nbTests;
  out.precision(12);

  in >> nbTests;
  getline(in, line);
  int keys[NBTYPE];
  int chesttype[NBCHEST];
  int sol[NBCHEST];
  vvi chestcontent(NBCHEST);

  for (int test=0; test<nbTests; test++) {
    
    int k, n, ki, tmp;
    in >> k >> n;
    vector<bool> stucked(1 + (1 << n), false);
    FOR(i,1,n+1) keys[i] = 0;
    FOR(i,0,k) {
      in >> tmp;
      assert(tmp >= 1 && tmp <= NBTYPE); /* I hope keys are numbered from 1 to (at most) the number of keys */
      keys[tmp]++;
    }
    FOR(chestnum, 1, n + 1) {
      in >> chesttype[chestnum] >> ki;
      chestcontent[chestnum] = vi(ki);
      FOR(i,0,ki) {
	in >> chestcontent[chestnum][i];
	assert(chestcontent[chestnum][i] >= 1 && chestcontent[chestnum][i] <= NBTYPE);
      }
    }
    stack<int> st;
    int current = 1; /* next chest to check */
    int state = 0;
    int newstate;
    int success = (1 << n) - 1;
  
    for(;;) {
      for(; current <= n; current++) {
	newstate = state | (1 << (current - 1));
	if ((newstate > state) && (keys[chesttype[current]] != 0) && (!stucked[newstate])) /* if this chest is not open yet,
								    we have a key to open this chest, 
								    and the new state is not known as stucked */
	  break;
      }
      if (current <= n) {
	st.push(current);
	keys[chesttype[current]]--;
	for (int i = 0; i < chestcontent[current].size(); i++)
	  keys[chestcontent[current][i]]++;
	state = newstate;
	current = 1;
	if (state == success)
	  break;
      } else {
	if (st.empty())
	  break;
	current = st.top();
	st.pop();
	keys[chesttype[current]]++;
	for (int i = 0; i < chestcontent[current].size(); i++)
	  keys[chestcontent[current][i]]--;
	stucked[state] = true;
	state = state ^ (1 << (current - 1));
	current++;
      }
    }
    out << "Case #" << test+1 << ": ";
    if (state == success) {
      int i = 0;
      while (!st.empty()) {
	sol[i++] = st.top(); 
	st.pop(); 
      }
      for(i = n - 1; i >= 0; i--)
	out << sol[i] << " ";
      out << endl;
    }
    else {
      assert (st.empty());
      out << "IMPOSSIBLE" << endl;
    }
  }
}

