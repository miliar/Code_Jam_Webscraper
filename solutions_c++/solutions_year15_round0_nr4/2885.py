// OminousOmino.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <stdint.h>
#include <fstream>
#include <sstream>
#include <string>


using namespace std;

struct TestCase
{
	uint16_t X;
	uint16_t R;
	uint16_t C;
};

vector<TestCase> parseInput(ifstream &input_stream)
{
	size_t test_cases_num = 0;
	vector<TestCase> test_cases;
	string line;

	getline(input_stream, line);
	istringstream iss(line);
	iss >> test_cases_num;

	for (size_t i = 0; i < test_cases_num; i++)
	{
		TestCase test_case;
		getline(input_stream, line);
		istringstream iss(line);
		iss >> test_case.X >> test_case.R >> test_case.C;

		test_cases.push_back(test_case);
	}
    
	return test_cases;
}

string solve(const TestCase& test_case)
{
	bool grid_can_be_filled = true;

    // If ominous size is greater than both of the
    // dimensions then there is certainly a way that the
    // grid cannot be filled
	if (test_case.X>test_case.R && test_case.X > test_case.C)
	{
		grid_can_be_filled = false;
	}
	else if ((test_case.R*test_case.C) % test_case.X != 0)
	{
		grid_can_be_filled = false;
	}
 	else// At least on of the grid dims exceeds ominous size
	{
		if (test_case.X == 1 || test_case.X == 2)
		{
			grid_can_be_filled = true;
		}
		if (test_case.X == 3&&(test_case.C==1||test_case.R==1))
		{
			grid_can_be_filled = false;
		}
		if (test_case.X == 4)
		{
			if ((test_case.R == 1 || test_case.C == 1) || 
				(test_case.R == 2 || test_case.C == 2))
				grid_can_be_filled = false;
		}

	}
    
	return grid_can_be_filled ? "GABRIEL" : "RICHARD";
}

void printResults(string output_file_name,const vector<string> &results)
{
	ofstream of(output_file_name);

	size_t case_num = 0;
	for (auto&result : results)
	{
		of << "Case #" << ++case_num << ": " << result << std::endl;
	}
	of.close();
}

int main(int argc, char* argv[])
{
	if (argc < 2){
		std::cout << "Error command argument missing!" << std::endl;
		return 1;
	}
	ifstream infile (argv[1]);

	vector<TestCase> test_cases = parseInput(infile);
	infile.close();
	
	vector<string> results;
	for (auto& test_case : test_cases)
	{
		results.push_back(solve(test_case));
	}

	printResults("outputfile.txt", results);

	return 0;
}

