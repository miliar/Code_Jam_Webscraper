/*
 * Q1.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: Neil
 */

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;


int test;

int grid[4][4];

int A;
int B;

vector<int> sol;
int cnt = 0;

int main() {


	freopen("test.in","r", stdin);
	freopen("Q1.out","w",stdout);
	cin >> test;

	for(int t = 0; t < test; t++) {
		cout << "Case #" << t + 1 << ": ";
		cnt = 0;
		sol.clear();

		cin >> A;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin >> grid[i][j];
				if(A - 1 == i) {
					sol.push_back(grid[i][j]);
				}
			}
		}

		cin >> B;

		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin >> grid[i][j];
			}
		}

		int ans = 0;

		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(sol[i] == grid[B - 1][j]) {
					cnt++;
					ans = sol[i];
				}
			}
		}


		if(cnt == 0) {
			cout << "Volunteer cheated!" << endl;
		} else if(cnt == 1) {
			cout << ans << endl;
		} else if(cnt > 1) {
			cout << "Bad magician!" << endl;
		}







	}

	return 0;
}


