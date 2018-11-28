// RankAndFile.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;


int main()
{
	int t;
	cin >> t;

	for (int c = 1; c <= t; ++c) {
		cout << "Case #" << c << ": ";

		int n;
		cin >> n;

		vector<vector<int> > lists;
		int numLists = (2 * n) - 1;
		for (int i = 0; i < numLists; ++i) {
			vector<int> l;
			for (int j = 0; j < n; ++j) {
				int x;
				cin >> x;
				l.push_back(x);
			}
			lists.push_back(l);
		}

		vector<vector<int> > pairs;
		unordered_set<int> seen;
		int missingIndex = -1;
		vector<int> checkVec;
		for (int i = 0; i < n; ++i) {
			int small1 = -1;
			int small2 = -1;

			for (int j = 0; j < lists.size(); ++j) {
				if (seen.count(j)) continue;

				if (small1 == -1) {
					small1 = j;
					continue;
				}

				if (lists[j][i] == lists[small1][i]) {
					small2 = j;
				}
				else if (lists[j][i] < lists[small1][i]) {
					small1 = j;
					small2 = -1;
				}
			}

			vector<int> n;
			n.push_back(small1);
			seen.insert(small1);
			if (small2 != -1) {
				n.push_back(small2);
				seen.insert(small2);
			}
			else {
				missingIndex = i;
				checkVec = lists[small1];
			}
			pairs.push_back(n);
		}

		for (int i = 0; i < pairs.size(); ++i) {
			if (pairs[i].size() == 2) {
				if (lists[pairs[i][0]][missingIndex] == checkVec[i]) {
					pairs[i].erase(pairs[i].begin());
				}
				else {
					pairs[i].erase(pairs[i].begin()+1);
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			cout << lists[pairs[i][0]][missingIndex] << " ";
		}

		cout << endl;

	}
    return 0;
}

