#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main() {
	int t;
	cin >> t;

	int c = 1;
	ofstream ofs ("RankAndFile.txt");
	while (t--) {
		int n;
		cin >> n;

		int x;
		map<int, int> cmap;
		for (int i = 0; i < 2*n-1; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> x;
				cmap[x]++;
			}
		}

		vector<int> vnum;

		for (map<int, int>::iterator itr = cmap.begin(); itr != cmap.end(); ++itr) {
			if (itr->second % 2 != 0) {
				vnum.push_back(itr->first);
			}
		}

		sort(vnum.begin(), vnum.end());

		ofs << "Case #" << c++ << ": ";
		for (int i = 0; i < n; ++i) {
			ofs << vnum[i] << " ";
		}
		ofs << endl;
	}
}