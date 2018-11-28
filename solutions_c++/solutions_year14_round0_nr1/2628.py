#include <fstream>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;


int main() {
	ifstream inf("A-small-attempt0.in");
	ofstream outf("output.txt");

	int T; inf >> T;
	for (int tc = 1; tc <= T; tc++) {
		outf << "Case #" << tc << ": ";

		int ans; inf >> ans;
		--ans;
		int cards[4][4];
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			inf >> cards[i][j];
		set<int> poss[2];
		for (int j = 0; j < 4; j++)
			poss[0].insert(cards[ans][j]);

		inf >> ans;
		--ans;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			inf >> cards[i][j];
		for (int j = 0; j < 4; j++)
			poss[1].insert(cards[ans][j]);

		vector<int> inter;
		set_intersection(poss[0].begin(), poss[0].end(), poss[1].begin(), poss[1].end(), back_inserter(inter));
		if (inter.size() == 0) outf << "Volunteer cheated!\n";
		else if (inter.size() > 1) outf << "Bad magician!\n";
		else outf << inter[0] << "\n";
	}
}