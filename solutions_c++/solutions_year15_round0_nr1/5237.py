// Store.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int countpeopleadd(string* people, int threshold, int currov) {
	if (threshold > (people->size() - 1))
		return 0;

	int currovadd = 0;

	int ptc = (int)((*people)[threshold] - '0');

	if (currov < threshold) {
		currovadd += threshold - currov;
		currov += threshold - currov;
	}

	currov += ptc;

	currovadd += countpeopleadd(people, threshold + 1, currov);

	return currovadd;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fc("input.txt");
	ofstream fo("output.txt", std::ofstream::out);

	int ncases;
	fc >> ncases;

	cout << "# Cases: " << ncases << endl;

	for (int i = 1; i <= ncases; i++) {
		int maxS;
		fc >> maxS;

		string people;
		fc >> people;

		fo << "Case #" << i << ": " << countpeopleadd(&people, 0, 0) << endl;
	}

	fo.close();
	fc.close();

	cout << "Done..." << endl;

	system("pause");

	return 0;
}

