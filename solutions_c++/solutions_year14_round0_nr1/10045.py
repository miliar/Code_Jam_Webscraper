#include "utility.h"
#include <iostream>
#include <fstream>

using namespace std;
using namespace utility;

vector<vector<int>> get_integers(vector<vector<string>> v)
{
	vector<vector<int>> numbers(4, vector<int>(4, 0));
	for (int i = 0; i < v.size(); i++)
	{
		for (int j = 0; j < v[i].size(); j++)
		{
			numbers[i][j] = Convert::to_integer(v[i][j]);
		}
	}
	return numbers;
}

string status(vector<int> a, vector<int> b)
{
	int count = 0;
	string message = "";
	for (int i = 0; i < a.size(); i++)
	{
		for (int j = 0; j < b.size(); j++)
		{
			if (a[i] == b[j])
			{
				count++;
			}
		}
	}

	if (count == 0)
	{
		message = "Volunteer cheated!";
	}
	if (count == 1)
	{
		for (int i = 0; i < a.size(); i++)
		{
			for (int j = 0; j < b.size(); j++)
			{
				if (a[i] == b[j])
				{
					message = Convert::to_string(a[i]);
				}
			}
		}
	}
	if (count > 1)
	{
		message = "Bad magician!";
	}

	return message;
}

int main()
{
	ifstream input;
	ofstream output;
	vector<vector<string>> data_first;
	vector<vector<string>> data_second;
	vector<vector<int>> numbers_first;
	vector<vector<int>> numbers_second;
	string line = "";
	int first_value = 0;
	int second_value = 0;

	input.open("A-small-attempt1.in");
	output.open("out.txt");
	getline(input, line);
	int count = Convert::to_integer(line, false);

	for (int i = 0; i < count; i++)
	{
		getline(input, line);
		first_value = Convert::to_integer(line);

		getline(input, line);
		data_first.push_back(strings::split(line, ' '));
		getline(input, line);
		data_first.push_back(strings::split(line, ' '));
		getline(input, line);
		data_first.push_back(strings::split(line, ' '));
		getline(input, line);
		data_first.push_back(strings::split(line, ' '));

		getline(input, line);
		second_value = Convert::to_integer(line);

		getline(input, line);
		data_second.push_back(strings::split(line, ' '));
		getline(input, line);
		data_second.push_back(strings::split(line, ' '));
		getline(input, line);
		data_second.push_back(strings::split(line, ' '));
		getline(input, line);
		data_second.push_back(strings::split(line, ' '));

		numbers_first = get_integers(data_first);
		numbers_second = get_integers(data_second);
		output << "Case #" << i + 1 << ": " << status(numbers_first[first_value - 1], numbers_second[second_value - 1]) << endl;

		data_first.clear();
		data_second.clear();
		numbers_first.clear();
		numbers_second.clear();
	}

	input.close();
	output.close();

	return 0;
}