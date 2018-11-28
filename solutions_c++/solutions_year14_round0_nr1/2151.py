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

int T, w, r, o, lo;
int nr[17];

int main (void) {
	cin >> T;
	for (int i = 1; i <= T; i++) {
		o = 0;
		for (int j = 1; j <= 16; j++) nr[j] = 0;
		cin >> w;
		for (int j = 1; j <= 4; j++)
		for (int k = 1; k <= 4; k++) {
			cin >> r;
			if (j == w) {
				nr[r]++;
				//cerr << r << " marked (2)\n";	
			}
		}
		cin >> w;
		for (int j = 1; j <= 4; j++)
		for (int k = 1; k <= 4; k++) {
			cin >> r;
			if (j == w) {
				nr[r]++;
				//cerr << r << " marked (2)\n";	
			}
			if (nr[r] == 2) {
				o++;
				lo = r;
				//cerr << r << " is possible\n";
			}
		}
		cout << "Case #" << i << ": ";
		if (o == 1)
			cout << lo << '\n';
		else if (o == 0)
			cout << "Volunteer cheated!\n";
		else
			cout << "Bad magician!\n";
	}
}
