#include <iostream>
#include <stdlib.h>
//#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iomanip>
#include <algorithm>
//#include <math.h>

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
			printf("%i\t", A[i][j]); 
		cout << endl;
	}
	return 0;
}


int print_array_double(double A[], int N) 
{
//#A is array of length N. no verification of inputs
	int i = 0;
	for (i = 0 ; i < ( N - 1); i++ )
	{	
		cout << A[i] << "\t" ;
	}
	cout << A[N-1] << endl;
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

int readfile(char * filename, double **** returnCases, int &returnNumCases, int ** returnCaseSizes)
{
	 //cout << "hey\n";
	int numCases;
	ifstream infile(filename);
	if (!infile) {
		cout << "problem with " << infile << " for reading." << endl;
		return 0;
	}
	infile >> numCases;
	double *** cases	=  new double**[numCases];
	int * caseSizes = new int[numCases];

	//cout << "numCases is " << numCases << endl;
	for (int i = 0 ; i < numCases; i++)
	{
		cases[i] = new double*[2];
		//cout << "hey 0\n";
		infile >> caseSizes[i];
		//cout << "hey 1\n";
		cases[i][0] = new double[caseSizes[i]];
		//cout << "hey 2\n";
		cases[i][1] = new double[caseSizes[i]];
		//cout << "hey 3\n";
		//Naomi's blocks
		for (int j = 0; j < caseSizes[i]; j++)
		{
			infile >> cases[i][0][j];
			//cout << "hey 4\n";
		}
		//cout << "hey 5\n";
		//Ken's blocks
		for (int j = 0; j < caseSizes[i]; j++)
			infile >> cases[i][1][j];
	}
	*returnCases = cases;
	returnNumCases = numCases;
	*returnCaseSizes = caseSizes;
	//cout << "Done reading file\n";
}


void solveCase(double ** iCase, int caseSize, int * solution)
{
	//naomi's blocks
	//cout << "hey0\n";
	sort(iCase[0], iCase[0] + caseSize);
	//ken's blocks
	sort(iCase[1], iCase[1] + caseSize);
	//print_array_double(iCase[0], caseSize);
	//print_array_double(iCase[1], caseSize);
	bool *naomiUsed = new bool[caseSize];
	bool *kenUsed   = new bool[caseSize];
	for (int i = 0; i < caseSize; i++)
	{
		naomiUsed[i] = false;
		kenUsed[i]   = false;
		
	}
	int wins0 = 0;
	int wins1 = 0;

	//deceitful war, 
	//assumes block sizes won't be equal, stated in problem
	int kenLowest = 0;
	int kenHighest = caseSize-1;
	int naomiLowest = 0;
	for (int i =0; i< caseSize; i++)
	{
		//cout << iCase[0][i] << " vs " << iCase[1][kenLowest] << endl;
		if (iCase[0][i] < iCase[1][kenLowest])
		{
			//cout << "Ken wins in Deceitful war, but plays his highest\n";
			kenHighest--;
			if (kenHighest < 0 && i < caseSize-1)
				cout << "problem with kenHighest\n";
		}
		else
		{
			//ken doesn't win, but he only loses his lowest card
			kenLowest++;
			if (kenLowest > caseSize-1 && i < caseSize-1)
				cout << "problem with kenLowest0\n";
			wins0++;
		}
			
	}

	//regular war
	//assumes block sizes won't be equal. stated in problem

	for (int i = 0; i < caseSize; i++)
	{
		naomiUsed[i] = false;
		kenUsed[i]   = false;
		
	}
	kenLowest = 0;
	kenHighest = caseSize-1;
	for (int i = caseSize-1; i>= 0;i--)
	{
		//cout << iCase[0][i] << " vs " << iCase[1][kenHighest] << endl;
		if (iCase[0][i] > iCase[1][kenHighest])
		{
			kenUsed[kenLowest] = true;
			//ken loses, so he plays his lowest
			while (kenUsed[++kenLowest]);
			if (kenLowest > caseSize-1 && i > 0)
				cout << "problem with kenLowest1\n";
			wins1++;
		}
		else
			//Ken wins. But, he finds the lowest value of he can play that will win
			for (int j = 0; j< caseSize; j++)
				if (!kenUsed[j] && iCase[1][j] > iCase[0][i])
				{
					kenUsed[j] = true;
					if (j == kenLowest) 
						while (kenUsed[--kenLowest]);
					else if (j == kenHighest) 
						while (kenUsed[--kenHighest]);
					j = caseSize;
				}
	}
	solution[0] = wins0;
	solution[1] = wins1;



	delete []naomiUsed;
	delete []kenUsed;
	//delete []timesToGetXCookiesWithNFarms;
	
					
}


int solve(double *** cases, int * caseSizes, int numCases, int ** solutions)
{
		//print_matrix(caseSizes, numCases, 2);
	//print_array(caseLengths, numCases);
	for (int i = 0; i < numCases; i++)  //outermost loop runs through each case
	{
		//solutions[i] = solveCase(cases[i]);
		solveCase(cases[i], caseSizes[i], solutions[i]);
		cout << "Case #" << i+1 << ": " << solutions[i][0] << " " << solutions[i][1] << endl;
	}
	//print_char_array(solutions, numCases);
}

int main(int argc, char * argv[])
{
	//myCase 	   = 93  - 1;
	//char ** solutions;

   if (&argc != NULL && argc > 0 && strcmp(argv[1], "-t") == 0)
   {
	int numTests = 11;
	//bool * testResults ;
	//testResults = runTests(numTests);
	for (int i =0; i< numTests; i++)
	{
		//cout << "test #" << i+1<< " results: " << testResults[i] << endl ;
	}	
	//delete []testResults;

   }			//cout << argv[1] << endl;
   else
   {
	char inpufile[] = "test.txt";
	int numCases;
	double *** cases;
	int * caseSizes;
	int ** solutions;


	//cout << "hey" << endl;
	readfile(inpufile, &cases, numCases, &caseSizes);
	//cout << "done reading file\n"; ;
	solutions = new  int*[numCases]();
	for (int i = 0; i< numCases; i++)
		solutions[i] = new int[2]();
	solve(cases, caseSizes, numCases, solutions);

	for (int i = 0; i < numCases; i++)
	{
		//print_array_doubles(cases[i], 3);
		//cout << endl;
		//print_matrix(cases[i][1], 4, 4);
		//cout << endl;
		//cout << "Case #" << i+1 << ": " << solutions[i][0] << " " << solutions[i][1] << endl;
	/*
		if (solutions[i] > 0)
			cout << solutions[i] << endl;
		else if (solutions[i] == 0)
			cout << "Bad magician!" << endl; 
		else
			cout << "Volunteer cheated!" << endl;
	*/
	}
		//print_matrix(cases[myCase], caseSizes[myCase][0], caseSizes[myCase][1]);
	delete [] solutions;
	//for (int i = 0; i < numCases; i++)
	//	delete [] cases[i];
	//delete [] cases;

	
   }
   return 0;
}
