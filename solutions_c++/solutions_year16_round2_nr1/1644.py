/*
 * A.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: nmarwan
 */

#include <iostream>
#include <sstream>
#include <set>
#include <algorithm>
#include <vector>
#include <memory.h>

using namespace std;

string w[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int wss = 10;

int main () {
	freopen ("A.in", "rt", stdin);
	freopen ("a.out", "wt", stdout);

	int t;
	cin >> t;
	for (int tt =1  ; tt <= t ; tt++){
		cout << "Case #" << tt << ": ";
		string s;
		cin >> s;

		vector<int> dig;
		int cnt[128];
		memset(cnt, 0, sizeof cnt);
		for (int i=0 ; i < s.size() ; i++) {
			cnt[s[i]] ++;
		}

		int key[] = { 0, 2, 4, 6, 8, 1, 3, 5, 7, 9 };
		int val[] = { 'Z', 'W', 'U', 'X', 'G', 'O', 'T', 'F', 'V', 'I' };
		int len = 0;
		for (int i=0 ; i < 10 ; i++) {
			int k = key[i];
			int ch = val[i];
			int d = cnt[ch];

			for (int j=0 ; j < d ; j++) {
				dig.push_back(k);
				len += w[k].size();
				for (int jj=0 ; jj < w[k].size() ; jj++) {
					cnt[w[k][jj]]--;
				}
			}
		}

		sort(dig.begin(), dig.end());

		for (int i=0; i < dig.size() ; i++) {
			cout << dig[i];
		}
		cout << endl;
	}
}
