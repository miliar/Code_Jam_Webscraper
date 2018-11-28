#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char** argv) {
	int CASE_NUM = 0;

	// open input file
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");

	// load case number
	fin >> CASE_NUM;
	cout << "Case number : " << CASE_NUM << endl;

	//CASE_NUM = 3;
	for (int ti = 1; ti <= CASE_NUM; ti++) {
		char input[2001] = {0, };
		int alpha['Z' + 1] = {0, };
		int num[10] = {0, };

		fin >> input;

		for (int i = 0; input[i] != 0; i++) {
			switch (input[i]) {
			case 'Z':
				alpha['E'] += -1;
				alpha['R'] += -1;
				alpha['O'] += -1;
				num[0]++;
				break;
			case 'W':
				alpha['T'] += -1;
				alpha['O'] += -1;
				num[2]++;
				break;
			case 'U':
				alpha['F'] += -1;
				alpha['O'] += -1;
				alpha['R'] += -1;
				num[4]++;
				break;
			case 'X':
				alpha['S'] += -1;
				alpha['I'] += -1;
				num[6]++;
				break;
			case 'G':
				alpha['E'] += -1;
				alpha['I'] += -1;
				alpha['H'] += -1;
				alpha['T'] += -1;
				num[8]++;
				break;
			default:
				alpha[ (int)input[i] ] += 1;
				break;
			}
		}

		// candidate : ONE, THREE, FIVE, SEVEN, NINE - unique char : T, S, H
		if (alpha['T'] > 0) {
			num[3] += alpha['T'];
			alpha['H'] += -1 * alpha['T'];
			alpha['R'] += -1 * alpha['T'];
			alpha['E'] += -1 * alpha['T'] * 2;
			alpha['T'] = 0;
		}

		// candidate : ONE, FIVE, SEVEN, NINE - unique char : S, F
		if (alpha['S'] > 0) {
			num[7] += alpha['S'];
			alpha['V'] += -1 * alpha['S'];
			alpha['N'] += -1 * alpha['S'];
			alpha['E'] += -1 * alpha['S'] * 2;
			alpha['S'] = 0;
		}

		// candidate : ONE, FIVE, NINE - unique char : F
		if (alpha['F'] > 0) {
			num[5] += alpha['F'];
			alpha['I'] += -1 * alpha['F'];
			alpha['V'] += -1 * alpha['F'];
			alpha['E'] += -1 * alpha['F'];
			alpha['F'] = 0;
		}

		// candidate : ONE, NINE - unique char : I
		if (alpha['I'] > 0) {
			num[9] += alpha['I'];
			alpha['N'] += -1 * alpha['I'] * 2;
			alpha['E'] += -1 * alpha['I'];
			alpha['I'] = 0;
		}

		// candidate : ONE - unique char : O N E
		if (alpha['O'] > 0) {
			num[1] += alpha['O'];
			alpha['N'] += -1 * alpha['O'];
			alpha['E'] += -1 * alpha['O'];
			alpha['O'] = 0;
		}


		fout << "Case #" << ti << ": ";
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < num[i]; j++)
				fout << i;
		fout << endl;
	}

	fin.close();
	fout.close();
}
