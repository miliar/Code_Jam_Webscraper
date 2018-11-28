/*
 * problem21.cpp
 *
 *  Created on: 03-May-2014
 *      Author: cfilt
 */
#include <cstring>
#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
int main() {
	int cases;
	cin >> cases;
	FILE* fout = fopen("out.txt", "w");
	bool flag;
	vector<pair<char, int> > vals[2];
	for (int i = 0; i < cases; ++i) {
		int N;
		cin >> N;
		string strs;

		flag = false;
		for (int j = 0; j < N; ++j) {
			cin >> strs;
			char c = strs[0];
			int count = 0;
			for (int k = 0; k < strs.length(); ++k) {
				if (c != strs[k]) {
					pair<char, int> p;
					p.first = c;
					p.second = count;
					vals[j].push_back(p);
					count = 0;
					c = strs[k];
				}
				count++;
			}
			pair<char, int> p;
			p.first = c;
			p.second = count;
			vals[j].push_back(p);
		}
		for (int j = 1; j < N; ++j) {
			if (vals[j - 1].size() != vals[j].size()) {
				fprintf(fout, "Case #%d: %s\n", i + 1, "Fegla Won");
				flag = true;
				break;
			}
		}
		if (flag) {
			for (int j = 0; j < N; ++j)
				vals[j].clear();
			continue;
		}

		int ans = 0;
		//For small only
		for (int k = 0; k < vals[0].size(); ++k) {
			if (vals[0][k].first != vals[1][k].first) {
				fprintf(fout, "Case #%d: %s\n", i + 1, "Fegla Won");
				flag = true;
				break;
			}
			ans += abs(vals[0][k].second - vals[1][k].second);
		}
		if (flag) {
			for (int j = 0; j < N; ++j)
				vals[j].clear();
			continue;
		}
		fprintf(fout, "Case #%d: %d\n", i + 1, ans);
		for (int j = 0; j < N; ++j)
			vals[j].clear();

	}
	return 0;
}
