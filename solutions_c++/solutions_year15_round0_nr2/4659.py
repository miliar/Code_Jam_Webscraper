#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int rec_best(map<int, int> plates);

int main() {
	int ncases;
	cin >> ncases;

	for (int c = 1; c <= ncases; c++) {
		map<int, int> plates;

		int n;
		cin >> n;

		for (int i = 0; i < n; i++) {
			int q;
			cin >> q;
			plates[q]++;
		}

		cout << "Case #" << c << ": " << rec_best(plates) << endl;
	}

	return 0;
}

int rec_best(map<int, int> plates) {
	/*{
		for (auto it = plates.cbegin(); it != plates.cend(); it++) {
			cout << it->first << ":" << it->second << ", ";
		}
		cout << endl;
	}*/

	if (plates.size() == 0 || plates.rbegin()->first == 0) {
		return 0;
	}
	if (plates.rbegin()->first == 1) {
		return 1;
	}

	int split_best;
	int dec_best;

	dec_best = plates.rbegin()->first;

	//split path
	{
		int val = plates.rbegin()->first;

		split_best = dec_best;

		vector<int> testvals;

		if (val > 3) {
			testvals.push_back(val / 2);
		}
		if (val > 8) {
			testvals.push_back(val / 3);
		}

		for (int newvala : testvals) {
			map<int, int> newplates_split(plates);

			int newvalb = val - newvala;

			newplates_split[val]--;
			newplates_split[newvala]++;
			newplates_split[newvalb]++;

			//filter zeros
			for (auto it = newplates_split.cbegin(); it != newplates_split.cend();) {
				if (it->first == 0 || it->second == 0) {
					newplates_split.erase(it++);
				} else {
					++it;
				}
			}

			split_best = min(rec_best(newplates_split) + 1, split_best);
		}
	}

	/*//dec path
	{
		map<int, int> newplates_dec;

		for (auto it = plates.cbegin(); it != plates.cend(); it++) {
			if (it->first != 1) {
				newplates_dec[it->first - 1] = it->second;
			}
		}

		dec_best = rec_best(newplates_dec) + 1;
	}*/

	return min(split_best, dec_best);
}