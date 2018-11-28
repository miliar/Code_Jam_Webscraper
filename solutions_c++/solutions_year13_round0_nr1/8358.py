#include <iostream>
#include <stdlib.h>
//#include <stdio.h>
#include <fstream>
#include <math.h>

using namespace std;



int print_char_array(char * A, int N) 
{
//#A is array of length N. no verification of inputs
	int i = 0;
	for (i = 0 ; i < ( N - 1); i++ )
	{	
		cout << A[i] << " ";
	}
	cout << A[N-1] << endl;
	return 0;
}


int print_char_matrix(char **A, int R, int C) 
{
//#A is maxtrix of R rows and C columns of length N. no verification of inputs
	int i = 0;
	for (i = 0 ; i < ( R); i++ )
	{	
		for (int j = 0; j < C; j++)
			cout << A[i][j] << " ";
		cout << endl;
	}
	return 0;
}
int print_matrix(int **A, int R, int C) 
{
//#A is maxtrix of R rows and C columns of length N. no verification of inputs
	int i = 0;
	for (i = 0 ; i < ( R); i++ )
	{	
		for (int j = 0; j < C; j++)
			printf("%i ", A[i][j]); 
		cout << endl;
	}
	return 0;
}


int print_array(int A[], int N) 
{
//#A is array of length N. no verification of inputs
	int i = 0;
	for (i = 0 ; i < ( N - 1); i++ )
	{	
		printf("%i ", A[i]); 
	}
	printf("%i\n", A[N-1]);
	return 0;
}

int getLength(char * input)
{
	int i=0;
	while (input[i] != '\0')
		i++;
	return i;

}



int readfile(char * filename, char **** returnCases, int * returnNumCases)
{
	int numCases;
	ifstream infile(filename);
	if (!infile) {
		cout << "problem with " << infile << " for reading." << endl;
		return 0;
	}
	infile >> numCases;
	char *blah = new char[1];
	
	char *** cases	= new char**[numCases];
	//cout << "numCases is " << numCases << endl;
	for (int i = 0 ; i < numCases; i++)
	{
		cases[i] = new char*[4];
		for (int j = 0; j < 4; j++)
		{
			cases[i][j] = new char[4];
			infile >> cases[i][j];
			//infile.getline(cases[i][j], 4);
			//print_char_array(cases[i][j], 4);
		}
			
		//if (i < numCases - 1)
			infile.getline(blah, 1);
	}
	*returnCases = cases;
	*returnNumCases = numCases;
	//cout << "Done reading file\n";
	//return void;
}

char solveCase(char ** iCase)
{
	//print_char_matrix(iCase, 4, 4);
	char solution = 'D';
	int win = 0;
	for (int i = 0; i < 4; i++)
	{
		char char1 = iCase[i][0];
		if (char1 == '.') {
			solution = 'G';
		}
		else {			
			// if i = 0 or 3, check diagonal, too
			if (i == 0) {
				char char2 = char1;
				for (int j = 1; j < 4; j++) {
					if (j == 1 && char1 == 'T')
						char2 = iCase[1][1];	
					else if (iCase[j][j] != char2 && iCase[j][j] != 'T') {
						win = 0;
						j = 4;
					}
					else if (j == 3) {
						win = 1;
						solution = char2;
						return char2;
					}
				}
			}
			else if (i == 3) {  // opposite diagonal
				char char2 = char1;
				for (int j = 1; j < 4; j++) {
					if (j == 1 && char1 == 'T')
						char2 = iCase[2][1];	
					else if (iCase[3-j][j] != char2 && iCase[3-j][j] != 'T') {
						win = 0;
						j = 4;
					}
					else if (j == 3) {
						win = 1;
						solution = char2;
						return char2;
					}
				}
			}

			//rows
			for (int j = 1; j  < 4; j++) {
				char char2 = char1;
				if (j == 1 && char1 == 'T') 
					char2 = iCase[i][1];
				else if (iCase[i][j] != char2 && iCase[i][j] != 'T') {
					win = 0;
					j = 4;
				}
				else if (j == 3) {
					win = 1;
					solution = char2;
					return solution;
				}
			}
		}
		//cols
		char1 = iCase[0][i];
		if (char1 == '.') {
			solution = 'G';
		}
		else {
			for (int j = 1; j  < 4; j++) {
				char char2 = char1;
				if (j == 1 && char1 == 'T') 
					char2 = iCase[1][i];
				else if (iCase[j][i] != char2 && iCase[j][i] != 'T') {
					win = 0;
					j = 4;
				}
				else if (j == 3) {
					win = 1;
					solution = char2;
					return solution;
				}
			}
		
		}
	}
	return solution;
}


int solve(char *** cases, int numCases, char * solutions)
{
	//print_array(caseLengths, numCases);
	for (int i = 0; i < numCases; i++)  //outermost loop runs through each case
	{
		solutions[i] = solveCase(cases[i]);
	}
	//print_char_array(solutions, numCases);
}

int main(void)
{
	//char ** solutions;
	char inpufile[] = "test.txt";
	int numCases;
	char *** cases;
	char * solutions;
	//cout << map['a'%32] << endl;	
	readfile(inpufile, &cases, &numCases);
	solutions = new  char[numCases];
	solve(cases, numCases, solutions);
	//cout << "done running solve function\n";

	
	for (int i = 0; i < numCases; i++)
	//for (int i = 0; i < 1; i++)
	{
		//cout << line << "hey" << endl;
		printf("Case #%d: ", i+1); 
//		cout << endl;
		//cout << solutions[i] << endl;
		if ( solutions[i] == 'X')
			cout << "X won";
		else if ( solutions[i] == 'O')
			cout << "O won";
		else if ( solutions[i] == 'D')
			cout << "Draw";
		else if ( solutions[i] == 'G')
			cout << "Game has not completed";
		else
			cout << "problem";
		cout << endl;
	}
	return 0;
}
