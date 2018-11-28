#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>

#pragma comment(linker, "/STACK:133217728")

using namespace std;

int best;
void go(vector <int> xx, int step = 0) {
	//if(xx.empty()) return 0;
	sort(xx.begin(), xx.end());
	reverse(xx.begin(), xx.end());
	best = min(best, step + xx[0]);
	if(step >= best) return;
	int res = xx[0];

	int k = xx[0];
	for(int i=1; i<=k/2; i++) {
		xx[0] = i;
		xx.push_back(k - i);
		go(xx, step + 1);
		xx.pop_back();
	}
}

int solve(vector <int>& x) {
	sort(x.begin(), x.end());
	best = x[x.size()-1];
	go(x);
	return best;
}
int main() {  
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		int n;
		vector <int> x;
		cin >> n;
		for(int i=0; i<n; i++) {
			int p;
			cin >> p;
			x.push_back(p);
		}

		cout << "Case #" << t << ": " << solve(x) << endl;
	}
    return 0;
}