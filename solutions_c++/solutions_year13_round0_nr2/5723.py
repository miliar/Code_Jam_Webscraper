/*
 * A.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Marwan
 */

#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstring>
#include <sstream>
#include <complex>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <climits>
#include <set>
#include <map>

using namespace std;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;
#define MP make_pair
#define SZ(x) (int)x.size()

int dcmp(double a, double b) {
	return (fabs(a - b) <= eps) ? 0 : ((a < b) ? -1 : 1);
}

typedef long long ll;
typedef pair<int, int> pii;

int di[] = { 0, 1};
int dj[] = { 1, 0};
vector<vector <int> > vs(4);
int N, M ;

bool checkRow (int i, int x){
	for (int j=0 ; j < M ; j++)
		if (vs[i][j] > x)
			return false;

	return true ;
}

bool checkCol (int j, int x){
	for (int i=0 ; i < N ; i++)
		if (vs[i][j] > x)
			return false ;
	return true ;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
//	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);
#endif
	int T;
	cin >> T;
	for (int tt = 0; tt < T; tt++) {
		cout << "Case #" << tt + 1 << ": ";
		cin >> N >> M ;

		vs.clear() ;
		vs.resize(N, vector <int>(M)) ;

		for (int i=0 ; i < N ; i++)
			for (int j=0 ; j < M ; j++)
				cin >> vs[i][j] ;

		int cnt = 0 ;
		for (int i=0 ; i < N ; i++)
			for (int j=0 ; j < M ; j++)
				cnt += (checkRow(i, vs[i][j]) || checkCol(j, vs[i][j])) ;

		if (cnt == N * M)
			cout << "YES" << endl ;
		else
			cout << "NO" << endl ;

	}
	return 0;
}
