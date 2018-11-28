#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <bitset>
#include <deque>

const long long LINF = (1e15);
const int INF = (1<<27);
#define EPS 1e-6
const int MOD = 1000000007;

using namespace std;

double calc(double C, double F, double X) {
	double ans = X / 2;
	int farm = (int)X;
	
	double res = 0;
	double f = 2.0;
	for (int i=0; i<farm; ++i) {
		ans = min(ans, res + X / f);
		res += C / f;
		f += F;
	}
	return ans;
}

int main() {
	ifstream ifs("/GoogleCodeJam/dat.txt");
	int Number;
	ifs >> Number;
	for (int i=1; i<=Number; ++i) {
    double C,F,X;
		ifs >> C >> F >> X;
		double ans = calc(C, F, X);
		printf("Case #%d: %.7lf\n", i, ans);
	}
	return 0;
}