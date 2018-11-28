#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>
#include <iostream>
#include <iomanip>

using namespace std;

#define INF (1<<29)
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define TIMESTAMP(x) eprintf("["#x"] Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)

double solve(double now, double C, double F, double X, double rate) {
	// Case 1
	double t1  = (X - now) / rate;
	
	// Case 2
	double tt, t2;
	tt = (C - now) / rate;
	rate += F;
	t2 = tt + X / rate;
	if(t2 < t1)
		t2 = tt + solve(0, C, F, X, rate);
	
	return min(t1, t2);
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		double C, F, X;
		cin >> C >> F >> X;
		cout << "Case #" << t << ": ";
		cout << fixed << setprecision(10) << solve(0.0, C, F, X, 2.0);
		cout << endl;
	}
	return 0;
}
