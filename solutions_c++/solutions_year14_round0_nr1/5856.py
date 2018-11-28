#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<int> ProcessLine(string _line)
{
	vector<int> line;

	int space_pos = _line.find(' ');
	line.push_back(atoi(_line.substr(0, space_pos).c_str()));

	_line = _line.substr(space_pos + 1);
	space_pos = _line.find(' ');
	line.push_back(atoi(_line.substr(0, space_pos).c_str()));

	_line = _line.substr(space_pos + 1);
	space_pos = _line.find(' ');
	line.push_back(atoi(_line.substr(0, space_pos).c_str()));

	_line = _line.substr(space_pos + 1);
	space_pos = _line.find(' ');
	line.push_back(atoi(_line.substr(0, space_pos).c_str()));

	return line;
}

int main()
{
	ofstream output;
	output.open("output.txt");

	ifstream input;
	input.open("A-small-attempt1.in");

	string temp = "";
	getline(input, temp);
	
	int test_cases = atoi(temp.c_str());
	for (int test = 0; test < test_cases; ++test)
	{
		// Process the first matrix
		getline(input, temp);
		int answer1 = atoi(temp.c_str());

		vector<int> possibles1;
		for (int i = 0 ; i < 4; ++i)
		{
			getline(input, temp);

			if (i == answer1 - 1)
				possibles1 = ProcessLine(temp);
		}

		// Process the second matrix
		getline(input, temp);
		int answer2 = atoi(temp.c_str());

		vector<int> possibles2;
		for (int i = 0 ; i < 4; ++i)
		{
			getline(input, temp);

			if (i == answer2 - 1)
				possibles2 = ProcessLine(temp);
		}

		// Compare the two vectors
		vector<int> answers;
		for (int i = 0; i < 4; ++i)
		{
			vector<int>::iterator val = find(possibles2.begin(), possibles2.end(), possibles1[i]);
			if (val != possibles2.end())
				answers.push_back(*val);
		}

		output << "Case #" << test + 1 << ": ";
		if (answers.size() <= 0)
			output << "Volunteer cheated!" << endl;
		else if (answers.size() == 1)
			output << answers[0] << endl;
		else
			output << "Bad magician!" << endl;
	}

	output.close();
	input.close();
	return 0;
}