/*
 * problem-D-small.cpp
 *
 *  Created on: Apr 12, 2015
 *  Author: Karim Mostafa
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <math.h> 
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ext/numeric>
#include <memory.h>
#include <valarray>
#include <limits>
using namespace std;

const int INF = numeric_limits<int>::max();

int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	int x, r, c;
	cin >> t;

	for (int i = 1; i <= t; i++) {
		cin >> x >> r >> c;

		if (x == 1)
			cout << "Case #" << i << ": " << "GABRIEL" << endl;
		else if (x == 2) {
			if ((r * c) % 2 == 0)
				cout << "Case #" << i << ": " << "GABRIEL" << endl;
			else
				cout << "Case #" << i << ": " << "RICHARD" << endl;
		} else if (x == 3) {
			if ((r * c) % 3 == 0) {
				if ((r == 1 && c == 3) || (r == 3 && c == 1))
					cout << "Case #" << i << ": " << "RICHARD" << endl;
				else
					cout << "Case #" << i << ": " << "GABRIEL" << endl;
			} else
				cout << "Case #" << i << ": " << "RICHARD" << endl;
		} else if (x == 4) {
			if ((r * c) % 4 == 0) {
				if ((r == 1 && c == 4) || (r == 4 && c == 1)
						|| (r == 2 && c == 2) || (r == 2 && c == 4) || (r == 4 && c == 2))
					cout << "Case #" << i << ": " << "RICHARD" << endl;
				else
					cout << "Case #" << i << ": " << "GABRIEL" << endl;
			} else
				cout << "Case #" << i << ": " << "RICHARD" << endl;
		}

	}

	return 0;
}
