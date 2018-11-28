#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <functional>
#include <numeric>
#include <algorithm>

using namespace std;

int T;
double C, F, X;

int main (void) {
	cin >> T;
	for (int i = 1; i<= T; i++) {
		cout << "Case #" << i << ": ";
		cin >> C >> F >> X;
		double prod = 2.0;
		double opt = X / prod;
		double tspent = 0.0;
		while (tspent < opt) {
			tspent += C / prod;
			prod += F;
			opt = min(opt, tspent + X / prod);
			if (prod > 10000000.0*F) {
				cerr << "Duurtlang!\n";
				break;
			}
		}
		cout.setf(ios::fixed); 
		cout.precision(7);
		cout << opt << '\n';
	}
}
