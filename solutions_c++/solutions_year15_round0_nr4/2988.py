#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_INPUT_BUFFER 100000
#define MAX_TOKENS 100000
#define INFINITY 1000000

int getParsedLine (ifstream &fin, vector <int> &input_vector)
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
			input_vector.push_back(atoi(token[i])); 
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
	vector <int> input_vector;
	
	fin.open("D:\\University\\code_jam\\projects\\qround_2015_D\\D-small-attempt0.in");
	fout.open("D:\\University\\code_jam\\projects\\qround_2015_D\\D-small-attempt0.out");
	//fin.open("D:\\University\\code_jam\\projects\\qround_2015_D\\test.in");
	//fout.open("D:\\University\\code_jam\\projects\\qround_2015_D\\test.out");

	getParsedLine(fin, input_vector);
	T = input_vector[0];

	for(int test_number = 1; test_number <= T; test_number++)
	{
		int X,R,C;
		getParsedLine(fin, input_vector);

		X = input_vector[0];
		R = input_vector[1];
		C = input_vector[2];

		if((R*C) % X)
		{
			fout << "Case #" << test_number << ": " << "RICHARD" << "\n";
			cout << "Case #" << test_number << ": " << "RICHARD" << "\n";
		}
		else
		{
			if(X == 1)
			{
				fout << "Case #" << test_number << ": " << "GABRIEL" << "\n";
				cout << "Case #" << test_number << ": " << "GABRIEL" << "\n";
			}
			else if(X == 2)
			{

				fout << "Case #" << test_number << ": " << "GABRIEL" << "\n";
				cout << "Case #" << test_number << ": " << "GABRIEL" << "\n";
				
			}
			else if(X == 3)
			{
				if(R < 2 || C < 2)
				{
					fout << "Case #" << test_number << ": " << "RICHARD" << "\n";
					cout << "Case #" << test_number << ": " << "RICHARD" << "\n";
				}
				else
				{
					fout << "Case #" << test_number << ": " << "GABRIEL" << "\n";
					cout << "Case #" << test_number << ": " << "GABRIEL" << "\n";
				}
			}
			else if(X == 4)
			{
				if(R <= 2 || C <= 2)
				{
					fout << "Case #" << test_number << ": " << "RICHARD" << "\n";
					cout << "Case #" << test_number << ": " << "RICHARD" << "\n";
				}
				else
				{
					fout << "Case #" << test_number << ": " << "GABRIEL" << "\n";
					cout << "Case #" << test_number << ": " << "GABRIEL" << "\n";
				}
			}
		}
	}
	fout.close();
	fin.close();
	getchar();
	return 0;
}