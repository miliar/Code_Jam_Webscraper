#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	int length;
	string input;
	infile >> length;
	vector <string> inputs;
	int alphabets[15];
	vector <int> numbers;

	for (int i = 0; i < 15; ++i)
	{
		alphabets[i] = 0;
	}

	for (int i = 0; i < length; ++i)
	{
		infile >> input;
		inputs.push_back(input);
	}

	for(int i = 0; i < length; i++){
		input = inputs[i];

		for (int j = 0; j < input.length(); ++j)
		{
			if (input[j] == 'E')
			{
				alphabets[0] = alphabets[0] + 1;
			}
			else if (input[j] == 'F')
			{
				alphabets[1] = alphabets[1] + 1;
			}
			else if (input[j] == 'G')
			{
				numbers.push_back(8);
				alphabets[0] = alphabets[0] - 1;
				alphabets[4] = alphabets[4] - 1;
				alphabets[3] = alphabets[3] - 1;
				alphabets[9] = alphabets[9] - 1;

			}
			else if (input[j] == 'H')
			{
				alphabets[3] = alphabets[3] + 1;
			}
			else if (input[j] == 'I')
			{
				alphabets[4] = alphabets[4] + 1;
			}
			else if (input[j] == 'N')
			{
				alphabets[5] = alphabets[5] + 1;
			}
			else if (input[j] == 'O')
			{
				alphabets[6] = alphabets[6] + 1;
			}
			else if (input[j] == 'R')
			{
				alphabets[7] = alphabets[7] + 1;
			}
			else if (input[j] == 'S')
			{
				alphabets[8] = alphabets[8] + 1;
			}
			else if (input[j] == 'T')
			{
				alphabets[9] = alphabets[9] + 1;
			}
			else if (input[j] == 'U')
			{
				numbers.push_back(4);
				alphabets[7] = alphabets[7] - 1;
				alphabets[1] = alphabets[1] - 1;
				alphabets[6] = alphabets[6] - 1;
			}
			else if (input[j] == 'V')
			{
				alphabets[11] = alphabets[11] + 1;
			}
			else if (input[j] == 'W')
			{
				numbers.push_back(2);
				alphabets[9] = alphabets[9] - 1;
				alphabets[6] = alphabets[6] - 1;
			}
			else if (input[j] == 'X')
			{
				numbers.push_back(6);
				alphabets[8] = alphabets[8] - 1;
				alphabets[4] = alphabets[4] - 1;
			}
			else if (input[j] == 'Z')
			{
				numbers.push_back(0);
				alphabets[0] = alphabets[0] - 1;
				alphabets[7] = alphabets[7] - 1;
				alphabets[6] = alphabets[6] - 1;
			}
		}

		if (alphabets[8] != 0)
		{
			for (int l = 0; alphabets[8] > 0; ++l)
			{
				numbers.push_back(7);
				alphabets[8] = alphabets[8] - 1;
				alphabets[0] = alphabets[0] - 2;
				alphabets[11] = alphabets[11] - 1;
				alphabets[5] = alphabets[5] - 1;
			}
		}
		if (alphabets[1] != 0)
		{
			for (int l = 0; alphabets[1] > 0; ++l)
			{
				numbers.push_back(5);
				alphabets[0] = alphabets[0] - 1;
				alphabets[1] = alphabets[1] - 1;
				alphabets[4] = alphabets[4] - 1;
				alphabets[11] = alphabets[11] - 1;
			}
		}
		if (alphabets[3] != 0)
		{
			for (int l = 0; alphabets[3] > 0; ++l)
			{
				numbers.push_back(3);
				alphabets[0] = alphabets[0] - 2;
				alphabets[3] = alphabets[3] - 1;
				alphabets[7] = alphabets[7] - 1;
				alphabets[9] = alphabets[9] - 1;
			}

		}
		if (alphabets[6] != 0)
		{
			for (int l = 0; alphabets[6] > 0; ++l)
			{
				numbers.push_back(1);
				alphabets[0] = alphabets[0] - 1;
				alphabets[5] = alphabets[5] - 1;
				alphabets[6] = alphabets[6] - 1;
			}
		}
		if (alphabets[4] != 0)
		{
			for (int l = 0; alphabets[4] > 0; ++l)
			{
				numbers.push_back(9);
				alphabets[4] = alphabets[4] - 1;
				alphabets[5] = alphabets[5] - 2;
				alphabets[0] = alphabets[0] - 1;
			}
		}


		sort(numbers.rbegin(), numbers.rend());
		reverse(numbers.begin(),numbers.end());
		outfile << "Case #"<< i+1 << ": ";

		for (int l = 0; l < numbers.size(); ++l)
		{
			outfile << numbers[l];
		}
		outfile << endl;

		numbers.clear();
		for (int j = 0; j < 15; ++j)
		{
			alphabets[j] = 0;
		}
	}

	return 0;
}