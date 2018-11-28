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
#define pb push_back

vector<int> v;
int nr[2000001][102];
int n;

int solve(int a, int i) {
	//cout << a << " " << i <<  " " << v[i] << endl;
	if (i==n) {
		nr[a][i] = 0;
		return 0;
	}
	if (nr[a][i] != -1) return nr[a][i];

	if (a > v[i]) {
		int x= a + v[i];
		if ( x > 2000000) x = 2000000;
		solve(x,i+1);
		nr[a][i] = nr[x][i+1];
		return nr[a][i];
	}


	solve(a, i+1);
	nr[a][i] = nr[a][i+1] + 1;
//	nr[a][i] = n-i;

	if (v[i] > 1) {
		solve(a+a-1, i);
		nr[a][i] = min(nr[a+a-1][i] + 1, nr[a][i]);
	}
	return nr[a][i];
}

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

	int ttt;cin >> ttt;string ss;getline(cin, ss);

	for (int tt = 1; tt <= ttt; tt++) {
		int a;
		cin >> a >> n;
		v.clear();
		v.resize(n);
		for (int i = 0; i < n; ++i) cin >> v[i];

		sort(v.begin(), v.end());


		for (int i = 0; i < 2000001; i++)
			for (int j = 0; j < 102; j++)
				nr[i][j] = -1;
		
		int x = solve(a,0);
		cout << "Case #" << tt << ": " << x << endl; 
	}

	return 0;
}

