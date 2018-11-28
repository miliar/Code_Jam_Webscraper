#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

#define INFL "in"
#define OUTFL "out"

using namespace std;

void read() {
}

int tests;
int mat1[4][4], mat2[4][4];
int line1, line2;

void solve() {
	cin >> tests;
	
	for(int t=1; t<=tests; ++t) {
		cin >> line1;
		--line1;
		for(int i=0; i<4; ++i)
			for(int j=0; j<4; ++j) cin >> mat1[i][j];

		cin >> line2;
		--line2;
		for(int i=0; i<4; ++i)
			for(int j=0; j<4; ++j) cin >> mat2[i][j];				

		vector<int> v;
		for(int i=0; i<4; ++i)
			for(int j=0; j<4; ++j)
				if(mat1[line1][i] == mat2[line2][j])
					v.push_back(mat1[line1][i]);

		cout << "Case #" << t << ": ";
		if(v.size() == 0)
			cout << "Volunteer cheated!" << endl;
		else if(v.size() > 1)
			cout << "Bad magician!" << endl;
		else
			cout << v[0] << endl;
	}
}

int main() {
//#define ONLINE_JUDGE 1
#ifndef ONLINE_JUDGE
	freopen(INFL, "r", stdin);
	freopen(OUTFL, "w", stdout);
#endif

	read();
	solve();
	
	return 0;
}