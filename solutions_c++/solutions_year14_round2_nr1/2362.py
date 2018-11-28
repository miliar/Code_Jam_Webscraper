#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define forl(i,a,b) for(int i = a; i < b; ++i)

int main()
{
	int numcases = 0;
	cin >> numcases;
	forl(casei, 0, numcases) {
		int numlines;
		cin >> numlines;
		vector< pair<char,int> > data[100];
		cin >> ws;
		forl(linei, 0, numlines) {
			string line;
			getline(cin, line);
			data[linei].push_back(make_pair(line[0], 1));
			for(int i = 1; line[i] != '\0'; i++) {
				if (data[linei].back().first == line[i]) {
					data[linei].back().second++;
				} else {
					data[linei].push_back(make_pair(line[i], 1));
				}
			}
		}
		bool possible = true;
		forl(linei, 1, numlines) {
			if (data[linei].size() != data[linei-1].size()) {
				possible = false;
				break;
			}
			if (!possible) break;
			forl(i, 0, data[0].size()) {
				if (data[linei][i].first != data[linei-1][i].first) {
					possible = false;
					break;
				}
			}
		}
		if (possible) {
			int moves = 0;
			vector<int> aves;
			forl(i, 0, data[0].size()) {
				aves.push_back(0);
				forl(linei, 0, numlines) {
					aves.back() += data[linei][i].second;
				}
				aves.back() += numlines/2;
				aves.back() /= numlines;
			}
			forl(linei, 0, numlines) {
				forl(i, 0, data[0].size()) {
					int mov = data[linei][i].second - aves[i];
					if (mov < 0) mov *= -1;
					moves += mov;
				}
			}
			cout << "Case #" << (casei+1) << ": " << moves << endl;
		} else {
			cout << "Case #" << (casei+1) << ": Fegla Won" << endl;
		}
	}
	return 0;
}
