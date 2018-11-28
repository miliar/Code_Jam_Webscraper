/*
 * QR_C.cpp
 *
 *  Created on: 08/04/2016
 *      Author: fvonbergen
 */

#include "QR_C.h"

#include <cstdlib>
#include <string>
#include <vector>
#include <stdexcept>
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>

#define INITIAL_PRIME_NUMBERS_BASE 2

#define DELTA_SIEVING_BLOCK 32768	// It must be even. Related to the memory cache.

std::vector<unsigned long int> segmented_sieve(const unsigned long int & limit_number,const size_t & delta_sieving_block);
std::vector<unsigned long int> segmented_sieve(const unsigned long int & limit_number,const size_t & delta_sieving_block){
	std::vector<bool> aux_prime_numbers_sieving_block;
	std::vector<unsigned long int> prime_numbers;
	unsigned long int quant_sieving_blocks;
	double sqrt_limit_number;
	size_t i,j,k,aux_k;

	if(limit_number < delta_sieving_block)
		throw std::runtime_error("The limit number must be greater than the delta sieving block must be even.");
	if(delta_sieving_block%2)
		throw std::runtime_error("The delta sieving block must be even.");
	if(limit_number < 2)
		throw std::runtime_error("The limit number must be greater than 2.");
	// We need to search primes up to sqrt_limit_number.
	sqrt_limit_number = sqrt(limit_number);
	quant_sieving_blocks = ceil(limit_number/delta_sieving_block);
	for(i = 0;i < quant_sieving_blocks;i++){
		// First sieving block.
		if(i == 0){
			// Clean variable.
			aux_prime_numbers_sieving_block = std::vector<bool>(static_cast<unsigned long int>(delta_sieving_block/2),true);
			prime_numbers.push_back(2);
			for(j = 3;(j < delta_sieving_block) && (j < sqrt_limit_number);j = j + 2){
				if(aux_prime_numbers_sieving_block[(j + 1)/2] == true){
					for(k = 3*j;k < delta_sieving_block;k += 2*j){
						aux_prime_numbers_sieving_block[(k + 1)/2] = false;
					}
					prime_numbers.push_back(j);
				}
			}
			if(j > sqrt_limit_number){
				for(k = j;k < (i+1)*delta_sieving_block;k +=2){
					if(aux_prime_numbers_sieving_block[(k + 1)/2] == true){
						prime_numbers.push_back(k);
					}
				}
			}
		}
		// Other sieving blocks besides the first one.
		else{
			// Clean variable.
			aux_prime_numbers_sieving_block = std::vector<bool>(delta_sieving_block/2,true);
			for(j = 1;j < prime_numbers.size();j++){
				aux_k = (ceil(1.0*i*delta_sieving_block/prime_numbers[j])*prime_numbers[j]);
				for(k = (aux_k%2 ? aux_k : aux_k+prime_numbers[j]);k < (i+1)*delta_sieving_block;k += 2*prime_numbers[j]){
					aux_prime_numbers_sieving_block[(k - i*delta_sieving_block + 1)/2] = false;
				}
			}
			for(j = 1 + i*delta_sieving_block;(j < (i+1)*delta_sieving_block) && (j < sqrt_limit_number);j = j + 2){
				if(aux_prime_numbers_sieving_block[(j - i*delta_sieving_block + 1)/2] == true){
					for(k = 3*j;k < (i+1)*delta_sieving_block;k += 2*j){
						aux_prime_numbers_sieving_block[(k - i*delta_sieving_block + 1)/2] = false;
					}
					prime_numbers.push_back(j);
				}
			}
			if(j > sqrt_limit_number){
				for(k = j;k < (i+1)*delta_sieving_block;k += 2){
					if(aux_prime_numbers_sieving_block[(k - i*delta_sieving_block + 1)/2] == true){
						prime_numbers.push_back(k);
					}
				}
			}
		}
	}

	return prime_numbers;
}

int main(int argc,char * argv[]){
	std::ifstream input_file;
	std::ofstream output_file;
	std::string aux_file_line,input_filename,output_filename;
	std::vector<std::string> file_lines;
	size_t i,j,k,l,m,input_filename_extension_pos,aux_stoul;

	size_t prime_numbers_base;
	unsigned long long int quant_case_numbers,initial_jamcoin,jamcoin,aux_jamcoin;
	std::vector<unsigned long long int> jamcoin_lengths,quant_jamcoins,jamcoin_prime_numbers;
	std::vector<unsigned long int> prime_numbers;
	size_t aux_string_pos;
	std::string binary_jamcoin;
    char holder = ' ';

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
			throw std::runtime_error("The line has characters that aren't numbers.");
		for(i = 0;i < quant_case_numbers;i++){
			if((aux_string_pos = file_lines[i+QUANT_HEADER_LINES].find(' ')) != file_lines[i+QUANT_HEADER_LINES].rfind(' '))
				throw std::runtime_error("An NxJ line has an incorrect format.");
			jamcoin_lengths.push_back(std::stoul(file_lines[i+QUANT_HEADER_LINES].substr(0,aux_string_pos)));
			quant_jamcoins.push_back(std::stoul(file_lines[i+QUANT_HEADER_LINES].substr(aux_string_pos+1,file_lines[i+QUANT_HEADER_LINES].size()-1-aux_string_pos)));
		}
//		for(i = 0;i < quant_case_numbers;i++){
//			std::cout << jamcoin_length[i] << std::endl;
//			std::cout << quant_jamcoins[i] << std::endl;
//		}
		input_file.close();
		// Open output file.
		input_filename_extension_pos = input_filename.rfind(INPUT_FILENAME_EXTENSION);
		output_filename = input_filename;
		output_filename.replace(input_filename_extension_pos,std::string(INPUT_FILENAME_EXTENSION).size(),OUTPUT_FILENAME_EXTENSION);
		output_file.open(output_filename.c_str(),std::ofstream::out | std::ofstream::trunc);
		// Process the data.
		// Calculate prime numbers.
		prime_numbers_base = INITIAL_PRIME_NUMBERS_BASE;
		prime_numbers = segmented_sieve(pow(prime_numbers_base,*std::max_element(jamcoin_lengths.begin(),jamcoin_lengths.end())),DELTA_SIEVING_BLOCK);
		// Considering that numbers are primes in any base. Finding a composite number in any base is sufficient.
		for(i = 0;i < quant_case_numbers;i++){
			output_file << "Case #" << i+1 << ": " << std::endl;
			initial_jamcoin = pow(2,jamcoin_lengths[i]-1) + 1;
			jamcoin = initial_jamcoin;	// jamcoin is in base 2.
			for(j = 0;j < quant_jamcoins[i];j++){
				if(!(jamcoin < pow(2,jamcoin_lengths[i]))) // If I get in here is because I need more prime numbers.
						prime_numbers = segmented_sieve(pow(prime_numbers_base++,*std::max_element(jamcoin_lengths.begin(),jamcoin_lengths.end())),DELTA_SIEVING_BLOCK);
				for(k = 0;(k < prime_numbers.size()) && (prime_numbers[k] < jamcoin);k++){
					if(!(jamcoin%prime_numbers[k])){
						aux_jamcoin = jamcoin;
						binary_jamcoin.clear();
						while(aux_jamcoin != 0){
							holder = aux_jamcoin%2 + '0';
							binary_jamcoin = holder + binary_jamcoin;
							aux_jamcoin/=2;
						}
						break;
					}
				}
				if(k < prime_numbers.size() && (prime_numbers[k] < jamcoin)){
					// First we check if the number is a composite of the prime_numbers_base prime numbers.
					jamcoin_prime_numbers.clear();
					for(l = 2;l < 11;l++){
						aux_jamcoin = strtoull(binary_jamcoin.c_str(),NULL,l);
						for(m = 0;m < prime_numbers.size();m++){
							if(!(aux_jamcoin%prime_numbers[m])){
								jamcoin_prime_numbers.push_back(prime_numbers[m]);
								break;
							}
						}
						if(!(m < prime_numbers.size())){
							jamcoin = jamcoin + 2;
							j--;
							break;
						}
					}
					if(l == 11){
						output_file << binary_jamcoin;
						for(m = 0;m < jamcoin_prime_numbers.size();m++){
							output_file << ' ' << jamcoin_prime_numbers[m];
						}
						output_file << std::endl;
						jamcoin = jamcoin + 2;
					}
				}
				else{
					jamcoin = jamcoin + 2;
					j--;
				}
			}
			if(!(jamcoin < pow(2,jamcoin_lengths[i])))
				throw std::runtime_error("There are no composite numbers available for this case.");
		}

//		for(i = 0;(i < prime_numbers.size()) && (prime_numbers[i] < 100100);i++){
//			std::cout << prime_numbers[i] << "/";
//		}
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
