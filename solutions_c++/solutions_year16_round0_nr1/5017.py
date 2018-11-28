#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <string.h>
#include <fstream>
using namespace std;

int counters[10];

bool newNumberCheck(int num)
{
	int temp1, temp2;

	while (num!=0)
	{
		temp1 = num % 10;
		counters[temp1] ++;
		num = num / 10;
	}

	for (int i = 0; i < 10; i++)
	{
		if (counters[i] == 0)
		{
			return false;
		}
	}

	return true;
}

void resetCounters()
{
	for (int i = 0; i < 10; i++)
	{
		counters[i] = 0;
	}
}

int process(int number)
{
	int copy = number;

	if (number == 0)
		return -1;

	for (int i = 1; newNumberCheck(number) != true; i++)
	{
		number = copy*i;
	}


	return number;
}

void loadData(vector<int>&in)
{
	int total = 0;
	string line;
	ifstream myfile("large_input.txt");
	int i = 0;
	size_t ss;

	if (myfile.is_open())
	{
		while (!myfile.eof())
		{
			getline(myfile, line);

			if (line == "")
				continue;
			if (i != 0)
			{
				in.push_back(atoi(line.c_str()));
			}
			i++;
		}
		myfile.close();
	}
}

void output(vector<int>&out)
{
	ofstream myfile("large_output.txt");

	if (myfile.is_open())
	{
		for (int i = 0; i < out.size(); i++)
		{
			myfile << "Case #" << i + 1 << ": ";
			if (out[i] == -1)
				myfile << "INSOMNIA";
			else myfile << out[i];

			if (i != out.size() - 1)
			{
				myfile << endl;
			}
		}
		myfile.close();
	}
}


int main()
{
	vector<int> inputs;
	vector<int> outputs;

	loadData(inputs);

	for (int i = 0; i < inputs.size(); i++)
	{
		resetCounters();
		outputs.push_back(process(inputs[i]));
	}

	output(outputs);


	return 0;
}


