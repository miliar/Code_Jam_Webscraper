// Pancake.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "minmax.h"

using namespace std;

int maxind(vector<int>* diners) {
	int pimax = 0;
	for (int i = 0; i < diners->size(); i++) {
		if ((*diners)[i] > 0) {
			pimax = i;
		}
	}

	return pimax;
}

int dividetop(vector<int>* dinersarg, int t) {

	int maxpi = maxind(dinersarg);

	if (maxpi <= 1)
		return t + 1;
	else {
		int t1 = t + maxpi;

		int t2 = t1;
		for (int takeoff = 1; takeoff <= floor((double)maxpi / 2); takeoff++) {
			vector<int> newdinnerdis = *dinersarg;

			newdinnerdis[maxpi - takeoff] += (*dinersarg)[maxpi];
			newdinnerdis[takeoff] += (*dinersarg)[maxpi];
			int tn = t + (*dinersarg)[maxpi];
			newdinnerdis[maxpi] = 0;

			int tc = dividetop(&newdinnerdis, tn);
			//cout << "tc" << tc << endl;
			if (tc < t2)
				t2 = tc;
		}

		return(min(t1, t2));
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fc("input.txt");
	ofstream fo("output.txt", std::ofstream::out);

	int ncases;
	fc >> ncases;

	cout << "# Cases: " << ncases << endl;

	for (int i = 1; i <= ncases; i++) {
		int Ndiners;
		fc >> Ndiners;

		vector<int> diners(1001, 0);

		for (int j = 0; j < Ndiners; j++) {
			int Npan;
			fc >> Npan;

			diners[Npan]++;
		}

		fo << "Case #" << i << ": " << dividetop(&diners, 0) << endl;
	}

	fo.close();
	fc.close();

	cout << "Done..." << endl;

	system("pause");

	return 0;
}

