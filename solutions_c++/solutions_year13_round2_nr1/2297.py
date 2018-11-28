#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int eatMotes(int moteSize, vector<int>& moteList, int pl) {
	int mods = 10000, tmp;
//cout << moteSize << " " << moteList.size() << " " << pl << endl;
	for (; pl < moteList.size() && moteSize > moteList[pl]; ++pl) {
		moteSize += moteList[pl];
	}

	if (pl + 1 == moteList.size()) mods = 1;
	else if (pl < moteList.size()) {
		if (moteSize > 1) {
			mods = 1 + eatMotes(moteSize * 2 - 1, moteList, pl);
		}
		tmp = 1 + eatMotes(moteSize, moteList, pl + 1);
		mods = min(tmp, mods);
	} else {
		mods = 0;
	}

	return mods;
}

int main(void) {
	ifstream inf;
	ofstream outf;

	inf.open("motes.txt");
	outf.open("moteResults.txt");

	int cases, moteSize, numMotes, tmpMote;
	vector<int> moteList;

	inf >> cases;

	for (int i = 0; i < cases; ++i) {
		inf >> moteSize >> numMotes;

		moteList.clear();

		for (int j = 0; j < numMotes; ++j) {
			inf >> tmpMote;
			if (tmpMote < moteSize) {
				moteSize += tmpMote;
			} else {
				moteList.push_back(tmpMote);
			}
		}

		sort(moteList.begin(), moteList.end());
//cout << "case " << i << endl;
		outf << "Case #" << (i + 1) << ": " << eatMotes(moteSize, moteList, 0) << endl;
	}

	outf.close();
	inf.close();

	return 0;
}

