/*
 * codejam2014a.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: ahmedfarag
 */

#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iterator>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>

//#include<bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

#define ALL(x) (x).begin(),(x).end()
#define RALL(x) (x).rbegin(),(x).rend()
#define SZ(x) (int)(x).size()
#define MEMSET(x,val) memset((x),(val),sizeof(x))

#define OO 1e9
#define EPS 1e-9
const double PI = acos(-1);

#define MX 101
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
#endif

	int t, x[2], a[2][4][4], caseNo = 1;
	cin >> t;

	while (t--) {
		for (int k = 0; k < 2; ++k) {
			cin >> x[k];
			x[k]--;
			for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 4; ++j) {
					cin >> a[k][i][j];
				}
			}
		}
		int cnt = 0, common = -1;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (a[0][x[0]][i] == a[1][x[1]][j])
					cnt++, common = a[0][x[0]][i];
			}
		}
		printf("Case #%d: ", caseNo++);
		switch (cnt) {
		case 0:
			printf("Volunteer cheated!\n");
			break;
		case 1:
			printf("%d\n", common);
			break;
		default:
			printf("Bad magician!\n");

		}

	}

	return 0;
}

