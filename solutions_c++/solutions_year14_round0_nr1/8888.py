#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <utility>
#include <map>

using namespace std;

#define rep(i,j,k) for (int i = (int)j; i < (int)k;i++)
#define rep0(i,j) rep(i,0,j)

#define pb(a) push_back(a)

int T;

void solve(int n) {
	int r1, r2;
	int m1[4][4], m2[4][4];
	
	cin >> r1;
	rep0 (i,4) rep0 (j,4) cin >> m1[i][j];
	cin >> r2;
	rep0 (i,4) rep0 (j,4) cin >> m2[i][j];
	vector<int> row;
	
	rep0 (i,4) {
		row.pb(m1[r1-1][i]);
	}
	vector<int> res;
	rep0 (i,4) {
		rep0 (j,4) {
			if (m2[r2-1][i] == row[j]) {
				res.pb(row[j]);
			}
		}
	}
	
	if (res.size() == 0) {
		printf("Case #%i: Volunteer cheated!\n", n);
	} else if (res.size() == 1) {
		printf("Case #%i: %i\n", n, res[0]);
	} else {
		printf("Case #%i: Bad magician!\n",n);
	}
} 

int main() {
	
	freopen("A-small-attempt0.in.txt","r+",stdin);
	freopen("A-small-attempt0.out.txt","w", stdout);
	cin >> T;
	rep0 (i,T) {
		solve(i+1);
	}
}