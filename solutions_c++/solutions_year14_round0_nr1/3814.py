/************************************************************************************
"MagicTrick.cpp" - Problem A. Qualification Round 04/11/2014.
************************************************************************************/

#define MAX_ARGS 3
#define ARG_POS_IN 1
#define ARG_POS_OUT 2
#define MATRIX_DIM 4


#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;


int main(int argc, char* argv[])
{

	ifstream input_file;
	ofstream output_file;

	if (argc != MAX_ARGS) {
		cerr << "Usage: " << argv[0] << " <INPUT-FILE> <OUTPUT-FILE>" << endl;
		return EXIT_FAILURE;
	}

	input_file.open(argv[ARG_POS_IN]);
	output_file.open(argv[ARG_POS_OUT]);

	size_t T; // Amount of test cases.

	input_file >> T;

	for (size_t i=0; i<T; i++){
		size_t n_1, n_2;
		size_t matrix_1[MATRIX_DIM][MATRIX_DIM], matrix_2[MATRIX_DIM][MATRIX_DIM];

		//load data

		input_file >> n_1;

		for (size_t j=0; j<MATRIX_DIM; j++){
			for (size_t k=0; k<MATRIX_DIM; k++){
				input_file >> matrix_1[j][k];
			}
		}
	
		input_file >> n_2;

		for (size_t j=0; j<MATRIX_DIM; j++){
			for (size_t k=0; k<MATRIX_DIM; k++){
				input_file >> matrix_2[j][k];
			}
		}
		
		// evaluate
		size_t counter = 0;
		size_t card;

		for (size_t j=0; j<MATRIX_DIM; j++){
			for (size_t k=0; k<MATRIX_DIM; k++){
				if (matrix_1[n_1-1][j] == matrix_2[n_2-1][k]) {counter++; card=matrix_1[n_1-1][j];}
			}
		}

		output_file << "Case #" << i + 1 << ": ";

		switch (counter) 
		{
		case 0: output_file << "Volunteer cheated!" << endl;
			break;
		case 1: output_file << card << endl;
			break;
		default: output_file << "Bad magician!" << endl;
			break;
		}

	}
	
	input_file.close();
	output_file.close();	

	return EXIT_SUCCESS;
}

