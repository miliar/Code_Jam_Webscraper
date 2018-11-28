#include <iostream>
#include <vector>
#include<fstream>
using namespace std;

int main() {

	vector<int> first, second;

	ifstream input;

	input.open("input.in");

	ofstream output;

	output.open("out.out");

	int cases, ans1, ans2, temp; int index, index2;  int out;

	int count = 0; int inc = 1;
	input >> cases;


	while (inc <= cases)
	{
		input >> ans1;
		for (int i = 0; i<16; ++i)
		{
			input >> temp;
			first.push_back(temp);
		}

		input >> ans2;
		for (int i = 0; i<16; ++i)
		{
			input >> temp;
			second.push_back(temp);
		}

		if (ans1 == 1)
			index = 0;
		else
		if (ans1 == 2)
			index = 4;
		else
		if (ans1 == 3)
			index = 8;
		else
		if (ans1 == 4)
			index = 12;
		//-------------------------------------------------

		if (ans2 == 1)
			index2 = 0;
		else
		if (ans2 == 2)
			index2 = 4;
		else
		if (ans2 == 3)
			index2 = 8;
		else
		if (ans2 == 4)
			index2 = 12;

		// Comparing Loop
		for (int i = index; i<index + 4; ++i)
		for (int j = index2; j<index2 + 4; ++j)

		if (first[i] == second[j])
		{
			count++; out = first[i];
		}


		output << "Case #" << inc << ": ";

		if (count == 0)
			output << "Volunteer cheated!" << endl;
		else
		if (count>1)
			output << "Bad magician!" << endl;
		else
		if (count == 1)
			output<< out << endl;


		inc++; count = 0;

		first.clear();  second.clear();

	} // End cases loops

	return 0;
}