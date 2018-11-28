#ifndef CODE_JAM_HELPER_H
#define CODE_JAM_HELPER_H

#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>

//#define INFILE "D:\\University\\code_jam\\projects\\test.txt"
#define INFILE "D:\\University\\code_jam\\projects\\round1A_2015_A\\A-large.in"
#define OUTFILE "D:\\University\\code_jam\\projects\\round1A_2015_A\\A-large.out"
//#define OUTFILE "D:\\University\\code_jam\\projects\\test.out"

#define MAX_INPUT_BUFFER 10000
#define MAX_TOKENS 10000
#define INFINITY 10000

using namespace std;

/*
	description: takes a file input line and parses the numbers into an input vector
		fin -> input file stream
		input_vector -> vector containing the inputs from the input file
	return value: number of integers in the line
*/
// Overloaded function with int/double
int getParsedLine(ifstream &fin, vector <int> &input_vector);
int getParsedLine(ifstream &fin, vector <double> &input_vector);
int getParsedLine(ifstream &fin, vector <string> &input_vector);


// For converting an int vector to an array of binary
void convertIntVectorToBinaryVector(vector <string> input_vector, vector <vector <int>> &binary_vector, int digits);
// print output to file

#endif