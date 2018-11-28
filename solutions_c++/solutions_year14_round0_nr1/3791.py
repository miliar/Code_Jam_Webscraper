#include <iostream>
#include <stdlib.h>
//#include <stdio.h>
#include <fstream>
#include <string.h>
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



int readfile(char * filename, int ***** returnCases, int *** returnVolunteerAnswers, int &returnNumCases)
{
	int numCases;
	ifstream infile(filename);
	if (!infile) {
		cout << "problem with " << infile << " for reading." << endl;
		return 0;
	}
	infile >> numCases;
	int **** cases	=  new int***[numCases];
	int **volunteerAnswers = new int *[numCases];

	//cout << "numCases is " << numCases << endl;
	for (int i = 0 ; i < numCases; i++)
	{
		volunteerAnswers[i] = new int[2];
		infile >> volunteerAnswers[i][0];
		cases[i] = new int**[2];
		cases[i][0] = new int*[4];
		cases[i][1] = new int*[4];
		for (int j = 0; j< 4; j++)
		{
			cases[i][0][j] = new int[4];
			cases[i][1][j] = new int[4];
		}
		for (int j = 0; j < 4; j++)
			for (int k = 0; k <4; k++)
				infile >> cases[i][0][j][k];
		infile >> volunteerAnswers[i][1];
		for (int j = 0; j < 4; j++)
			for (int k = 0; k <4; k++)
				infile >> cases[i][1][j][k];
	}
	*returnCases = cases;
	*returnVolunteerAnswers = volunteerAnswers;
	returnNumCases = numCases;
	//*returnCaseSizes = caseSizes;
	//cout << "Done reading file\n";
	//return void;
}


int solveCase(int *** iCase, int * volunteerAnswers)
{
	int va1 = volunteerAnswers[0];
	int va2 = volunteerAnswers[1];
	int * rowEntries = new int[4];
	int answer;
	bool badMagician, cheat, success;
	for (int i = 0; i < 4; i++)
		rowEntries[i] = iCase[0][va1-1][i];

	//check for cheat (none of cards from row in first answer are in row for second answer
	//also check for bad magician (more than one of cards from row in first answer are in row for second answer
	cheat = true;
	badMagician = false;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			//cout << iCase[1][va2-1][i] << " " <<  rowEntries[j] << endl;
			if (iCase[1][va2-1][i] == rowEntries[j])
			{
				if (cheat == true)
				{
					//cout << "hey \n";
					cheat = false;
					answer = rowEntries[j];
				}
				else   //already found one match. Second is bad magician
				{
					badMagician = true;
					//cout << "hey bad magician\n";
				}
			}
		}
	}
	if (badMagician)
		return 0;
	else if (cheat)
		return -1;
	else
		return answer;
					
}


int solve(int **** cases, int numCases, int ** volunteerAnswers, int * solutions)
{
		//print_matrix(caseSizes, numCases, 2);
	//print_array(caseLengths, numCases);
	for (int i = 0; i < numCases; i++)  //outermost loop runs through each case
	{
		solutions[i] = solveCase(cases[i], volunteerAnswers[i]);
		//cout << "Case #" << i+1 << ": " << solutions[i] << endl;
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
	bool * testResults ;
	//testResults = runTests(numTests);
	for (int i =0; i< numTests; i++)
	{
		cout << "test #" << i+1<< " results: " << testResults[i] << endl ;
	}	
	delete []testResults;

   }			//cout << argv[1] << endl;
   else
   {
	char inpufile[] = "test.txt";
	int numCases;
	int **** cases;
	int * solutions;
	int ** volunteerAnswers;


	//cout << "hey" << endl;
	readfile(inpufile, &cases, &volunteerAnswers, numCases);
	//cout << "done reading file\n"; ;
	solutions = new  int[numCases];
	solve(cases, numCases, volunteerAnswers, solutions);
	for (int i = 0; i < numCases; i++)
	{
		//print_matrix(cases[i][0], 4, 4);
		//cout << endl;
		//print_matrix(cases[i][1], 4, 4);
		//cout << endl;
		cout << "Case #" << i+1 << ": ";
		if (solutions[i] > 0)
			cout << solutions[i] << endl;
		else if (solutions[i] == 0)
			cout << "Bad magician!" << endl; 
		else
			cout << "Volunteer cheated!" << endl;
	
	}
		//print_matrix(cases[myCase], caseSizes[myCase][0], caseSizes[myCase][1]);
	delete [] solutions;
	//for (int i = 0; i < numCases; i++)
	//	delete [] cases[i];
	//delete [] cases;

	
   }
   return 0;
}
