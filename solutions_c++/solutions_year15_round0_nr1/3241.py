#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
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
#include <sstream>


#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm> 

using namespace std;

void doit() {
	int Smax, Tot, G, nr;
	char r;
	Tot = 0;
	G = 0;
	cin >> Smax;
	for (int i = 0; i <= Smax; i++) {
		cin >> r;
		nr = r - '0';
		if (Tot < i) {
			G++;
			Tot++;
		}
		Tot += nr;
	}
	cout << G << '\n';
}

int main () {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		doit();
	}
	return 0;
}


