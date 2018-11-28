#pragma once

#include "StdAfx.h"
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>

class ReadInputFile
{

	std::ifstream infile;

public :	
	
	ReadInputFile ()
	{}

	void init (std::string inputFile)
	{
		infile.open(inputFile);
	}

	bool ReadNextTestCase ( int number_of_lines_per_test_case, std::vector<std::string> &test_case )
	{
		std::string line;
		if ( !std::getline (infile, line) )
			return false;

		test_case.push_back(line);
		int number_of_lines_to_read = number_of_lines_per_test_case - 1;

		while ( number_of_lines_to_read >= 1 )
		{
			if ( !std::getline (infile, line) )
				break;

			test_case.push_back(line);
			
			std::cout << "Line: " << line << std::endl;
			
			number_of_lines_to_read--;
		}

		if ( number_of_lines_to_read != 0 )
			return false;

		return true;
	}

	bool ReadEmptyLine ()
	{
		std::string line;
		if ( !std::getline (infile, line) )
			return false;

		return true;
	}


	bool ReadNextTestCase (std::vector<std::string> &test_case)
	{
		std::string line;
		if ( !std::getline (infile, line) )
			return false;

		test_case.push_back(line);
		int number_of_lines_to_read = atoi(line.c_str());
		
		while ( number_of_lines_to_read >= 1 )
		{
			if ( !std::getline (infile, line) )
				break;

			test_case.push_back(line);

			number_of_lines_to_read--;
		}
		
		if ( number_of_lines_to_read != 0 )
			return false;

		return true;
	}

	bool ReadNumberOfTestCases (int& number_of_test_cases )
	{
		std::string line;
		if ( !std::getline (infile, line) )
			return false;

		number_of_test_cases = atoi(line.c_str ());
		
		return true;
	}

	void CloseFile ()
	{
		infile.close();
	}


	void split(const std::string &s, char delim, std::vector<int> &elems) 
	{
	    std::stringstream ss(s);
	    std::string item;
	    while(std::getline(ss, item, delim)) {
	        elems.push_back( atoi(item.c_str()));
		}
	}

	void split(const std::string &s, char delim, std::vector<std::string> &elems) 
	{
	    std::stringstream ss(s);
	    std::string item;
	    while(std::getline(ss, item, delim)) {
	        elems.push_back(item.c_str());
		}
	}

};

