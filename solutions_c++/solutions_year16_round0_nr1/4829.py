/*
 * QR_A.cpp
 *
 *  Created on: 08/04/2016
 *      Author: fvonbergen
 */

#include "QR_A.h"

#include <cstdlib>
#include <string>
#include <vector>
#include <stdexcept>
#include <iostream>
#include <fstream>



int main(int argc,char * argv[]){
	std::ifstream input_file;
	std::ofstream output_file;
	std::string aux_file_line,input_filename,output_filename;
	std::vector<std::string> file_lines;
	size_t i,j,k,l,input_filename_extension_pos,aux_stoul;
	unsigned long int aux_uli;

	unsigned int quant_case_numbers;
	std::vector<unsigned long int> case_numbers;
	std::vector<bool> digits_appeared(10,0);
	std::string output_number;

	// Set exceptions for input/output operations.
	input_file.exceptions(std::ifstream::failbit | std::ifstream::badbit);
	try{
		// Check command line arguments.
		if(argc != QUANT_ARGC)
			throw std::runtime_error("The quantity of arguments of the invoked program is incorrect.");
		// Open input file.
		input_filename = argv[ARGV_INPUT_FILE_POS];
		input_file.open(input_filename.c_str(),std::ifstream::in);
		// Load file on string vector.
		while(!input_file.eof()){
			try{
				std::getline(input_file,aux_file_line);
			}
			catch(std::ifstream::failure const & exception){
				if(!input_file.eofbit | !input_file.failbit)
					throw std::runtime_error("The quantity of arguments of the invoked program is incorrect.");
			}
			file_lines.push_back(aux_file_line);
		}
		// Process the input file.
		quant_case_numbers = std::stoul(file_lines[FIRST_INPUT_LINE],&aux_stoul,10);
		if(aux_stoul != file_lines[FIRST_INPUT_LINE].size())
			throw std::runtime_error("The line has characters where there should be only numbers.");
		for(i = 0;i < quant_case_numbers;i++){
			aux_uli = std::stoul(file_lines[i+QUANT_HEADER_LINES],&aux_stoul,10);
			if(aux_stoul != file_lines[i+QUANT_HEADER_LINES].size())
				throw std::runtime_error("The line has characters where there should be only numbers.");
			case_numbers.push_back(aux_uli);
		}
		input_file.close();
		// Open output file.
		input_filename_extension_pos = input_filename.rfind(INPUT_FILENAME_EXTENSION);
		output_filename = input_filename;
		output_filename.replace(input_filename_extension_pos,std::string(INPUT_FILENAME_EXTENSION).size(),OUTPUT_FILENAME_EXTENSION);
		output_file.open(output_filename.c_str(),std::ofstream::out | std::ofstream::trunc);
		// Process the data.
		for(i = 0;i < quant_case_numbers;i++){
			if(!case_numbers[i]){
				output_file << "Case #" << i+1 << ": " << INSOMNIA_STR << std::endl;
			}
			else{
				for(j = 1;;j++){
					output_number = std::to_string(j*case_numbers[i]);
					for(k = 0;k < output_number.size();k++){
						aux_uli = output_number[k] - '0';
						if(aux_uli > 9)
							throw std::runtime_error("The character is not a valid digit.");
						digits_appeared[aux_uli] = 1;
					}
					for(k = 0;k < digits_appeared.size();k++){
						if(digits_appeared[k])
							continue;
						else
							break;
					}
					if(k == digits_appeared.size()){
						output_file << "Case #" << i+1 << ": " << output_number << std::endl;
						for(l = 0;l < digits_appeared.size();l++)
							digits_appeared[l] = 0;
						break;
					}
				}
			}
		}

		// Close output file
		output_file.close();

		return EXIT_SUCCESS;
	}
	catch(std::ifstream::failure const & exception) {
	    std::cerr << "Exception: " << exception.what() << std::endl;

	    return EXIT_FAILURE;
	}
	catch(std::invalid_argument const & exception){
	    std::cerr << "Exception: " << exception.what() << std::endl;

	    return EXIT_FAILURE;
	}
	catch(std::exception const & exception){
	    std::cerr << "Exception: " << exception.what() << std::endl;

	    return EXIT_FAILURE;
	}
}
