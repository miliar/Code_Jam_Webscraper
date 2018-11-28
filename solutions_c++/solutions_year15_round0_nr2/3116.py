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
	set < pair<int, int> > pc;
	set < pair<int, int> >::iterator it;
	pair<int, int> pa;
	int D, P;
	int div[1234];
	int Porig[1234];
	cin >> D;
	//cerr << "Read D = " << D << '\n';
	for (int d = 0; d < D; d++) {
		cin >> P;
		div[d] = 1;
		Porig[d] = P;
		pc.insert(make_pair(P,d));
		//cerr << "Added " << P << " at " << d << '\n';
	}
	int opt = 1234;
	int rem = 0;
	while (rem < opt) {
		pa = *(pc.rbegin());
		pc.erase(pa);
		opt = min(opt, rem + pa.first);
		//cerr << "opt is now min of " << opt << " and " << rem+pa.first << "\n";
		int j = pa.second;
		div[j]++;
		rem++;
		pc.insert(make_pair( (Porig[j] + div[j] - 1) / div[j] , j)); 
		//cerr << "Now divide " << j << " by " << div[j] << " to get " << (Porig[j] + div[j] - 1) / div[j] << '\n';
	}
	cout << opt << '\n';
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


