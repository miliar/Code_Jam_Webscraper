//============================================================================
// Name        : Part_elf.cpp
// Author      : von Bergen, Federico
// Version     :
// Copyright   :
// Description :
//============================================================================

#include <fstream>
#include <ios>
#include <iostream>
using std::cerr;
using std::endl;
#include <string>
#include <cstring>
#include <stdexcept>
#include <cstdlib>
#include <cmath>
#include <vector>
//#include <algorithm>

#include "Part_elf.h"
#include "defines.h"

/*Functions*/
unsigned int gcd (unsigned int first_number,unsigned int second_number);
unsigned int gcd (unsigned int first_number,unsigned int second_number){
    return (second_number == 0) ? first_number : gcd(second_number,first_number % second_number);
}


int main(void){
	std::ifstream input_file(INPUT_FILENAME,std::ifstream::in);
	std::ofstream output_file(OUTPUT_FILENAME,std::ifstream::out);
	std::string line;
	std::size_t substr_start = 0,substr_end = std::string::npos,i;
	std::vector< std::vector<std::string> > case_information(LINES_PER_CASE);
	std::vector<std::string> aux;
	char ** endptr = NULL;
	std::size_t quant_test_cases,case_number,elf_generation;
	unsigned int dividend,divisor,gcd_result;
	double aux_double;
	bool is_possible = 0;

	try{
		if(input_file.fail())
			throw std::runtime_error("The input file couldn't be opened.");
		if(output_file.fail())
			throw std::runtime_error("The output file couldn't be opened.");
		getline(input_file,line);
		quant_test_cases = strtol(line.c_str(),endptr,10);
		if(endptr != NULL)
			throw std::runtime_error("The input file is incorrect.");
		if(quant_test_cases < MIN_QUANT_TEST_CASES || quant_test_cases > MAX_QUANT_TEST_CASES)
			throw std::runtime_error("The number of cases isn't within the limits.");
		for(case_number = 0;input_file.good() && case_number < quant_test_cases;case_number++){
			/*Read from input file.*/
			for(i = 0;i < LINES_PER_CASE;i++){
				getline(input_file,line);
				substr_start = 0;
				substr_end = line.find(INPUT_FILE_DELIMITER,substr_start);
				if(substr_end == std::string::npos)
					case_information[i].push_back(line.c_str());
				else
					case_information[i].push_back(line.substr(substr_start,substr_end));
				while(substr_end != std::string::npos){
					substr_start = ++substr_end;
					substr_end = line.find(INPUT_FILE_DELIMITER,substr_start);
					case_information[i].push_back(line.substr(substr_start,substr_end-substr_start));
				}
			}
			/*Validate and load dividend and divisor.*/
			if(case_information[DIVIDEND_DIVISOR_POS].size() == 1){
				/*Validate dividend.*/
				substr_start = 0;
				substr_end = case_information[DIVIDEND_DIVISOR_POS][0].find(DIVIDEND_DIVISOR_DELIMITER,substr_start);
				dividend = strtol(case_information[DIVIDEND_DIVISOR_POS][0].substr(substr_start,substr_end).c_str(),endptr,10);
				if(endptr != NULL)
					throw std::runtime_error("The input file is incorrect.");
				if(dividend < MIN_DIVIDEND_DIVISOR || dividend > MAX_DIVIDEND_DIVISOR)
					throw std::runtime_error("The dividend isn't within the limits.");
				/*Validate divisor.*/
				substr_start = substr_end + 1;
				substr_end = case_information[DIVIDEND_DIVISOR_POS][0].size() - 1;
				divisor = strtol(case_information[DIVIDEND_DIVISOR_POS][0].substr(substr_start,substr_end).c_str(),endptr,10);
				if(endptr != NULL)
					throw std::runtime_error("The input file is incorrect.");
				if(divisor < MIN_DIVIDEND_DIVISOR || divisor > MAX_DIVIDEND_DIVISOR)
					throw std::runtime_error("The divisor isn't within the limits.");
				if(dividend > divisor)
					throw std::runtime_error("The dividend can't be greater than the divisor.");
			}
			else{
				throw std::runtime_error("The input file is incorrect.");
			}

			/*Check if possible.*/
			is_possible = true;
			aux_double = pow(2,MAX_GENERATIONS)*dividend/divisor;
			if(aux_double - floor(aux_double) != 0){
				is_possible = false;
			}

			/*Recalculate dividend and divisor.*/
			gcd_result = gcd(divisor,dividend);
			if(gcd_result != 1){
				dividend /= gcd_result;
				divisor /= gcd_result;
			}

			if(is_possible != false){
				for(i = 0;i < MAX_GENERATIONS;i++){
					if(double(dividend)/double(divisor) < 0.5){
						divisor /= 2;
						continue;
					}
					else{
						elf_generation = i + 1;
						break;
					}
				}
			}

			/*Write to output file.*/
			if(is_possible != false)
				output_file << "Case" << CHAR_SPACE << CHAR_NUMBER_SIGN << case_number + 1 << CHAR_COLON << CHAR_SPACE << elf_generation << endl;
			else
				output_file << "Case" << CHAR_SPACE << CHAR_NUMBER_SIGN << case_number + 1 << CHAR_COLON << CHAR_SPACE << "impossible" << endl;
			/*Clear information to use the information variable again.*/
			for(i = 0;i < LINES_PER_CASE;i++){
				case_information[i].clear();
			}
			case_information.clear();
		}
		getline(input_file,line);	/*Read the last empty line.*/
		if(!input_file.eof())
			throw std::runtime_error("There was an error reading the input file.");
		input_file.close();
		output_file.close();
		if(quant_test_cases != case_number)
			throw std::runtime_error("The input file doesn't contain the amount of cases declared in the header.");
	}
	catch(std::runtime_error & exception){
		cerr << "Part_elf:" << CHAR_SPACE << exception.what() << endl;
		return EXIT_FAILURE;
	}
	return EXIT_SUCCESS;
}
