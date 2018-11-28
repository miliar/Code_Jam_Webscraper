//============================================================================
// Name        : deceitful_war.cpp
// Author      : Vasilis Pardalis
// Version     :
// Copyright   :
//============================================================================

#include <iostream>
#include <iomanip>
#include <list>
#include <stdlib.h>
#include <cstdio>

using namespace std;


void errmsg(const char *msg) {

	cout << msg << endl;
	exit(EXIT_FAILURE);
}



int wins_war(list<double> naomi, list<double> ken) {

	int iWins = 0;
	double chosen_naomi, chosen_ken;

	while (naomi.size() > 0) {
		chosen_naomi = naomi.back();
		if (ken.back() > chosen_naomi) chosen_ken = ken.back();
		else {chosen_ken = ken.front(); iWins++;}
		naomi.remove(chosen_naomi);
		ken.remove(chosen_ken);
	}

	return iWins;
}


int wins_deceitful_war(list<double> naomi, list<double> ken) {

	int iWins = 0;
	list<double>::iterator p;
	double chosen_naomi, chosen_ken;

	while (naomi.size() > 1) {
		chosen_naomi = 0;
		chosen_ken = ken.front();
		for (p = naomi.begin(); p != naomi.end(); p++) {
			if (*p > chosen_ken) {chosen_naomi = *p; iWins++; break;}

		}
		if (chosen_naomi == 0) chosen_naomi = naomi.front();
			naomi.remove(chosen_naomi);
			ken.remove(chosen_ken);
		}

		if (naomi.front() > ken.front()) iWins++;

	return iWins;
}


int main() {


	double chosen_naomi, chosen_ken, told_naomi;
	int iCases;

	cin >> iCases;
	if (iCases > 0) {
		for (int i = 0; i < iCases; i++) {

			int iBlocks = 0, iWar_wins = 0, iDecWar_wins = 0;
			list<double> naomi_blocks;
			list<double> ken_blocks;


			cin >> iBlocks;

			for (int j = 0; j < iBlocks; j++) {
				double fTmp;
				cin >> fTmp;
				naomi_blocks.push_back(fTmp);
			}

			for (int j = 0; j < iBlocks; j++) {
				double fTmp;
				cin >> fTmp;
				ken_blocks.push_back(fTmp);
			}


			naomi_blocks.sort();
			ken_blocks.sort();

			iWar_wins = wins_war(naomi_blocks, ken_blocks);
			iDecWar_wins = wins_deceitful_war(naomi_blocks, ken_blocks);

			cout << "Case #" << (i + 1) << ": " << iDecWar_wins << " " << iWar_wins << endl;

		}


	}
	else errmsg("No test cases defined!");

	return 0;
}
