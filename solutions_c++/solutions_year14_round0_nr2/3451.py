#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

int main() {
	int tc;
	cin >> tc;
	for(int t = 0; t < tc; t++) {
		double C, F, X;
		cin >> C >> F >> X;
		int f = (F * X - 2 * C) / (C * F);
		if (X <= C) f = 0;
		if (f < 0) f = 0;		
		double T = X / (2 + f * F);
		for (int ff = 1; ff < f + 1; ff++) {
			T += C / (2 + (ff - 1) * F);
		}
		printf("Case #%d: %.7f\n", t + 1, T);
	}
}


