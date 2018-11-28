#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
#include <queue>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <stack>
#include <map>
#include <cassert>
#include <set>
#include <iomanip>
using namespace std;

#include "gmpxx.h"
typedef mpz_class big;

#define REP(i,n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define MP make_pair
#define PB push_back

//const int N = 15;
big n, p; //, high[N], low[N];

/* void process(int b, vector<int> x) {
	if (x.size() == 1) {
		high[ x[0] ] = max(high[ x[0] ], b);
		low[ x[0] ] = min(low[ x[0] ], b);
		return;
	}
	
	vector<int> win, loss;
	for (int i = 0; i < x.size(); i += 2) {
		if (x[i] < x[i+1]) {
			win.PB(x[i]);
			loss.PB(x[i+1]);
		} else {
			win.PB(x[i+1]);
			loss.PB(x[i]);
		}
	}
	process(b, win);
	process(b+win.size(), loss);
} */

int main() {
	int T;
	cin >> T;
	REP(qqq,T) {
		cin >> n >> p;
		
		big nn = 1;
		REP(i,n) nn *= 2;
		
		vector<big> v;
		
		big A = 0, B = 0;
		{
			big z = 2, h = 0, q = nn/2;
			
			big pp = 1;
			REP(i,n+1) {
				//v.PB(1<<i);
				//assert(( == pp);
				
				if (pp-1 >= 0)
					v.PB(pp-1);
				
				if (pp-2 >= 0)
					v.PB(pp-2);
				
				//if ((1<<i)+1 < nn)
				//	v.PB((1<<i)+1);
				
				pp *= 2;
			}
			v.PB(nn-1);
			sort(v.begin(), v.end());
			v.erase(unique(v.begin(), v.end()), v.end());
			
			REP(j,v.size()) {
				big i = v[j];
				
				if (i+1 == z) {
					z *= 2;
					h += q;
					q /= 2;
				}
				if (h < p)
					A = i;
			}
		}
		
		{
			big z = 2, h = nn-1, q = nn/2;
			
			REP(i,v.size()) v[i] = (nn-1)-v[i];
			
			REP(j,v.size()) {
				big i = v[j];
				
				if (((nn-1)-i)+1 == z) {
					z *= 2;
					h -= q;
					q /= 2;
				}
				if (h < p)
					B = max(B,i);
			}
		}
		
		//logic end
		cout << "Case #" << (qqq+1) << ": " << A << " " << B << endl;
	}
}
