#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;

vector< vector<int> > read() {
	vector< vector<int> > r(4, vector<int>(4));
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cin >> r[i][j];
		}
	}

	return r;
}



int main() {
	int _start = clock();

#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
#define taskname "cutting"
	//freopen(taskname".in","r",stdin);
    //freopen(taskname".out","w",stdout);
#endif
	
	int T;
	cin >> T;

	for (int test = 1; test <= T; ++test) {
		int r1, r2;
		vector< vector<int> > m1, m2;
		cin >> r1; m1 = read();
		cin >> r2; m2 = read();
		--r1; --r2;

		vector<int> v;
		sort(m1[r1].begin(), m1[r1].end());
		sort(m2[r2].begin(), m2[r2].end());

		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (m1[r1][i] == m2[r2][j]) {
					v.push_back(m1[r1][i]);
					m1[r1][i] = -1;
					m2[r2][j] = -1;
					break;
				}
			}
		}		
		printf("Case #%d: ", test);

		if (v.size() == 1) {
			cout << v[0] << endl;
			continue;
		}

		if (v.size() == 0) {
			cout << "Volunteer cheated!" << endl;
			continue;
		}

		if (v.size() > 1) {
			cout << "Bad magician!" << endl;
			continue;
		}
	}




	cerr << endl << endl << "Time: " << (double)(clock() - _start) / CLOCKS_PER_SEC << endl;
	return 0;
}