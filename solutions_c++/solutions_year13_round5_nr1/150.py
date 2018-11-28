#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <algorithm>
#include <climits>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <ctime>

using namespace std;

#define fname "A-large"
ifstream in(fname ".in");
ofstream out(fname ".out");

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
typedef long long ll;

ll B, A[37];
ll C[37];

void adjustIt(double &be, int n) {
	//FOR(i,0,37) cout << C[i] << " "; cout << endl;
	double nu = 0, su = 0;
	FOR(i,0,n) nu += C[i]-A[i];
	FOR(i,n,37) su += C[i]-A[i];
	double res = nu*(36-n);
	res /= n;
	res -= su;
	be = max(be,res);
}

void do_case(int case_number) {
	int N;
	in >> B >> N;
	FOR(i,0,N) in >> A[i];
	sort(A,A+N);
	reverse(A,A+N);
	FOR(i,N,37) A[i] = 0;
	reverse(A,A+37);
	double be = 0;
	FOR(n,1,36) {
		// choosing number of smallest
		//cout << "n = " << n << endl;
		ll cb = B;
		FOR(i,0,37) C[i]=A[i];
		ll ii = 0;
		FOR(i,0,n) {
			ii += C[n-1] - C[i];
			C[i] = C[n-1];
		}
		FOR(j,n,37) if(C[j] == C[n-1]) {
			ii++;
			C[j]++;
		} else break;
		if(ii > cb) continue;
		cb -= ii;
		ll t = C[n] - C[0] - 1;
		if(cb <= t*n) {
			t = cb / n;
			FOR(i,0,n) C[i] += t;
			cb -= t*n;
		} else {
			FOR(i,0,n) C[i] += t;
			cb -= t*n;
			while(1) {
				//FOR(i,0,37) cout << C[i] << " "; cout << endl;
				int m = 1;
				FOR(j,n+1,37) if(C[j] == C[j-1]) m++; else break;
				//cout << "  m = " << m << endl;
				if(n+m >= 36) break;
				ll r = C[n+m] - C[n];
				if(cb >= r*(n+m)) {
					FOR(j,0,n+m) C[j] += r;
					cb -= r*(n+m);
				} else {
					r = cb / (n+m);
					FOR(j,0,n+m) C[j] += r;
					cb -= r*(n+m);
					break;
				}
			}
		}
		adjustIt(be,n);
	}
	out << "Case #" << case_number << ": " << fixed << setprecision(9) << be << endl;
}

int main() {
	int T;
	in >> T;
	for(int it=1;it<=T;it++) do_case(it);
	in.close();
	out.close();
	return 0;
}