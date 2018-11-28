/*
ID: oooctav1
PROG: checker
LANG: C++
*/
#include <iostream> 
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <stack>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>

using namespace std;
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define mp make_pair


int main() {
//	freopen ("checker.out","w",stdout);
//	freopen ("checker.in","r",stdin);
	ios_base::sync_with_stdio(false);

/*
	int t;cin >> t;string ss;getline(cin, ss);
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": " << nrmax << endl; 
	}
*/

	int t;cin >> t;string ss;getline(cin, ss);

//	t = 60;
	for (int tt = 1; tt <= t; tt++) {
		int64_t r,t; cin >> r >> t;
//		r = 1; t = 1000000000000000000;
		int64_t area = 0, k;
		for (k = 1; area <= t; k++) 
			area += ((r << 1) + (k << 2) - 3);
		k--;k--;
		cout << "Case #" << tt << ": " << k << endl; 
	}

	return 0;
}

