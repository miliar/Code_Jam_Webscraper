#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (int argc, char *argv[]) {
	int questions, blocks, lost, lostDeceit, lostWar;
	double tmp;
	vector<double> naomi;
	vector<double>::iterator nit;
	vector<double> ken;
	vector<double>::iterator kit;
	cin >> questions;
	for (int i = 1; i <= questions; ++i) {
		cin >> blocks;
		for (int j = 0; j < blocks; ++j) {
			cin >> tmp;
			naomi.push_back(tmp);
		}
		for (int j = 0; j < blocks; ++j) {
			cin >> tmp;
			ken.push_back(tmp);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		lost = 0;
		for (nit = naomi.begin(), kit = ken.begin(); nit != naomi.end(); ++nit) {
			while (kit != ken.end() && *kit <= *nit) ++kit;
			if (kit == ken.end()) break;
			++kit;
			++lost;
		}
		lostWar = blocks - lost;
		reverse(naomi.begin(), naomi.end());
		reverse(ken.begin(), ken.end());
		lost = blocks;
		for (nit = naomi.begin(), kit = ken.begin(); nit != naomi.end(); ++nit, ++kit) {
			while (kit != ken.end() && *kit >= *nit) ++kit;
			if (kit == ken.end()) break;
			--lost;
		}
		lostDeceit = blocks - lost;
		cout << "Case #" << i << ": " << lostDeceit << " " << lostWar << endl;
		naomi.clear();
		ken.clear();
	}
}
