#include <fstream>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;



int solve(int p, int q)
{
	//cout << p << "/" << q << endl;

	int nb = 0;
	while (p < q) {
		if (q % 2 != 0) return 0;
		q >>= 1;
		++nb;
	}

	while (q != 1) {
		if (q % 2 != 0) return 0;
		q >>= 1;
	}

	return nb;
}

void main()
{
	ifstream input_file("input.txt");
	ofstream output_file("output.txt");

	int nbCases;
	input_file >> nbCases;

	for (int i = 1; i <= nbCases; ++i) {

		string input;
		getline(input_file, input, '/');

		int p = atoi(input.c_str());

		getline(input_file, input);
		int q = atoi(input.c_str());

		int result = solve(p, q);

		if (result) {
			output_file << "Case #" << i << ": " << result << endl;
		}
		else {
			output_file << "Case #" << i << ": " << "impossible" << endl;
		}
	}
}