#define _USE_MATH_DEFINES

#include <algorithm>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>

#define SREP(s,i,n) for(int i=s;i<(int)(n);++i)
#define REP(i,a) SREP(0,i,a)
#define ALL(a) (a).begin(),(a).end()

#define CLR(a) memset(a,0,sizeof(a))
#define REMOVE_AT(v,i) v.erase(v.begin()+i)

using namespace std;
const double EPS = 1e-8;
const double D_INF = 1e12;
const int I_INF = 1 << 29;
typedef long long LL;

int main(){
	int T;
	cin >> T;
	REP(tc, T) {
		int Sm;
		string inp;
		cin >> Sm >> inp;
		int sum = 0;
		int friends = 0;
		REP(i, inp.size()) {
			if (sum < i) {
				friends += (i - sum);
				sum += (i - sum);
			}
			sum += inp[i] - '0';
		}
		cout << "Case #" << (tc + 1) << ": " << friends << endl;
	}
	return 0;
}