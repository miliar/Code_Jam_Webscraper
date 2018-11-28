#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

std::vector<int> v1, v2, v3, vs;
// i,j,k = 2,3,4

int getVal(char a) {
	return (a - 'i') + 2;
}

int compute(int a, int b) {
	int sign = 1;
	if (a < 0) a = -a, sign = -sign;
	if (b < 0) b = -b, sign = -sign;
	if (a == 1) {
		sign *= b;
	} else if (a == 2) {
		switch(b) {
			case 1: sign *= 2;	break; 
			case 2: sign *= -1; break; 
			case 3: sign *= 4; break; 
			case 4: sign *= -3; break; 
		}
	} else if (a == 3) {
		switch(b) {
			case 1: sign *= 3;	break; 
			case 2: sign *= -4; break; 
			case 3: sign *= -1; break; 
			case 4: sign *= 2; break; 
		}
	} else if (a == 4) {
		switch(b) {
			case 1: sign *= 4;	break; 
			case 2: sign *= 3; break; 
			case 3: sign *= -2; break; 
			case 4: sign *= -1; break; 
		}
	}
	return sign;
}

int computeX(int a, LL x) {
	int sign = 1;
	if (a < 0) {
		a = -a;
		if (x % 2 == 0) sign = 1;
		else sign = -1;
	}
	if (a == 1) {
	} else {
		x = x % 4;
		if (x == 1) {
			sign *= a;
		} else if (x == 2) {
			sign *= -1;
		} else if (x == 3) {
			sign *=-a;
		} else if (x == 0) {
			sign *= 1;
		}
	}
	return sign; 
}

void computeValues(int start, std::vector<int> & value) {
	if (start >= value.size()) {
		value[value.size() - 1] = 1;
		return;
	}
	value[start] = vs[start];
	REP(i, start + 1, vs.size()) {
		value[i] = compute(value[i-1], vs[i]);
	}
	// REP(i, 0, value.size()) cerr<<value[i]<<" "; cerr<<"\n";
}


int main() {
  clock_t startTime = clock();
  ios_base::sync_with_stdio(false);

  int t; cin>>t; 
  for (int test = 1; test <= t; test++) {
  	cout<<"Case #"<<test<<": ";
  	LL l, x; cin>>l>>x;
  	string s; cin>>s;
  	string ss;
  	REP(i, 0, min(x, (LL)10)) {
  		ss += s;
  	}
  	// cout<<ss<<"\n";
  	x -= min(x, (LL)10);
  	v1.clear(); v2.clear(); v3.clear(); vs.clear();
  	v1.resize(ss.size());
  	v2.resize(ss.size());
  	v3.resize(ss.size());
  	
  	REP(i, 0, ss.size()) {
  		vs.push_back(getVal(ss[i]));
  	}
  	assert(vs.size() == v1.size());
  	computeValues(0, v1);
  	
  	LL pi = -1, pj = -1, pk = -1;
  	REP(i, 0, v1.size()) {
  		if (v1[i] == 2) {
  			pi = i; break;
  		}
  	}
  	bool possible = true;
  	if (pi != -1) {
  		computeValues(pi + 1, v2);
  		REP(i, pi + 1, v2.size()) {
  			if (v2[i] == 3) {
  				pj = i; break;
  			}
  		}
  		if (pj != -1) {
  			computeValues(pj + 1, v3);
  			REP(i, pj + 1, v3.size()) {
  				if (v3[i] == 4) {
  					pk = i; break;
  				}
  			}
  			if (pk != -1) {
  				v3.clear(); v3.resize(ss.size());
  				computeValues(pk + 1, v3);
  				int finalVal = v3[v3.size() - 1];
  				int lval = v1[s.size() - 1];
  				int leftval = computeX(lval, x);
  				// cout<<finalVal<<" "<<lval<<" "<<leftval<<" "<<x<<"\n";
  				finalVal = compute(finalVal, leftval);
  				// cout<<finalVal<<"\n";
  				if (finalVal != 1) {
  					possible = false;
  				}
  			} else possible = false;
  		} else possible = false;
  	} else possible = false;
  	if (possible) cout<<"YES\n";
  	else cout<<"NO\n";
  }

  clock_t endTime = clock();
  cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
  return 0;
}