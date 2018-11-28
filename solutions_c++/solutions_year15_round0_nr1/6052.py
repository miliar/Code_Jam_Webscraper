// StandingOvation.cpp : Defines the entry point for the console application.
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
	size_t maxShyness;
	vector<uint16_t> shynessCount;
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
		iss >> test_case.maxShyness;
		string shyeness_count;
		iss >> shyeness_count;
		for (auto& c : shyeness_count)
			test_case.shynessCount.push_back(static_cast<uint16_t>(c - '0'));

		test_cases.push_back(test_case);
	}
    
	return test_cases;
}

uint32_t solve(const TestCase& test_case)
{
	uint32_t standing = 0;
	uint32_t friend_num = 0;

	for (size_t level = 0; level < test_case.maxShyness + 1; ++level)
	{
        // If we have at least one persong in the audience
        // with this shyness level
		if (test_case.shynessCount[level])
		{
			if (level > standing)
			{
                //Invite sum more friends
				friend_num += level - standing;
                //Add them to the standing ovation crowd				
				standing += (level - standing);
			}

			standing += test_case.shynessCount[level];
		}
	}
	return friend_num;
}

void printResults(string output_file_name,const vector<uint32_t> &results)
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
	
	vector<uint32_t> results;
	for (auto& test_case : test_cases)
	{
		results.push_back(solve(test_case));
	}

	printResults("C:\\Users\\marcello\\Downloads\\outputfile.txt", results);

	return 0;
}

