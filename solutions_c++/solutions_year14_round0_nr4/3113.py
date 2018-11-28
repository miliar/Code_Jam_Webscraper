#include <algorithm>
#include <iostream>
#include <vector>

typedef unsigned int uint;

using namespace std;

void readBlocks(vector<double> &vec, int blocks) {
	for(int i = 0; i < blocks; ++i)
		cin >> vec[i];
}

uint solveWar(vector<double> &v1, vector<double> &v2) {
	uint v1_pos = 0, v2_pos = 0;

	while(v2_pos < v2.size())
		if(v2[v2_pos++] > v1[v1_pos])
			++v1_pos;

	return v1.size() - v1_pos;
}

uint solveDWar(vector<double> &v1, vector<double> &v2) {
	return v2.size() - solveWar(v2, v1);
}

int main() {
	int cases, blocks;

	cin >> cases;

	for(int i = 0; i < cases; ++i) {
		cout << "Case #" << i+1 << ": ";

		cin >> blocks;

		vector<double> naomi(blocks), ken(blocks);

		readBlocks(naomi, blocks);
		readBlocks(ken, blocks);

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		cout << solveDWar(naomi, ken) << " " << solveWar(naomi, ken) << endl;
	}

	return 0;
}
