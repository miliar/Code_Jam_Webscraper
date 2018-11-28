#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include "../code_jam_helper/code_jam_helper.h"

#define MAX_INPUT_BUFFER 10000
#define MAX_TOKENS 10000
#define INFINITY 1000000

using namespace std;

int getParsedLine (ifstream &fin, vector <string> &input_vector)
{
	char buf[MAX_INPUT_BUFFER];
	char *token[MAX_TOKENS] = {};
	int i = 0;
	if(!fin.is_open())
	{
		printf("Cannot get parsed line: input file cannot be opened\n");
		return 0;
	}

	// Delete all members (now size 0)
	input_vector.clear();

	// Make sure the input stream is not eof and is in a good state before doing anything
	if(fin.good())
	{
		fin.getline(buf, MAX_INPUT_BUFFER);
		if(buf == NULL)
		{
			printf("Reached end of file or cannot get line\n");
			return 0;
		}
		token[0] = strtok(buf, " ");
		for(i = 0; token[i] != NULL; i++)
		{
			input_vector.push_back(string(token[i])); 
			token[i+1] = strtok(NULL, " ");
		}
	}
	return i;
}

int main()
{
	ofstream fout;
	ifstream fin;
	int T;
	int Smax;
	
	//vector <int> shyness_vector;
	vector <string> input_vector;

	fin.open("D:\\University\\code_jam\\projects\\qround_2015_A\\A-large.in");
	fout.open("D:\\University\\code_jam\\projects\\qround_2015_A\\A-large.out");

	getParsedLine(fin, input_vector);
	T = atoi(input_vector[0].c_str());

	for(int test_number = 1; test_number <= T; test_number++)
	{
		int current_standing = 0;
		int Si = 0;
		int injected_friends = 0;
		getParsedLine(fin, input_vector);
		Smax = atoi(input_vector[0].c_str());

		// Actual algorithm starts here to calculate how many friends we need to inject
		for(int shyness = 0; shyness <= Smax; shyness++)
		{
			Si = input_vector[1].c_str()[shyness] - '0';
			if(shyness == 0)
			{
				current_standing = Si;
			}
			else
			{
				if(shyness <= current_standing)
				{
					current_standing += Si;
					continue;
				}
				else
				{
					injected_friends += shyness - current_standing;
					current_standing += Si + shyness - current_standing;
				}
			}
		}
		fout << "Case #" << test_number << ": " << injected_friends << "\n";
		cout << "Case #" << test_number << ": " << injected_friends << "\n";
	}
	fout.close();
	fin.close();
	return 0;
}