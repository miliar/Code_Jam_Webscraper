#include <iostream>
#include <stdlib.h>
//#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iomanip>
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


int print_array_doubles(double A[], int N) 
{
//#A is array of length N. no verification of inputs
	int i = 0;
	for (i = 0 ; i < ( N - 1); i++ )
	{	
		cout << A[i] << " " ;
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

int readfile(char * filename, double *** returnCases, int &returnNumCases)
{
	int numCases;
	ifstream infile(filename);
	if (!infile) {
		cout << "problem with " << infile << " for reading." << endl;
		return 0;
	}
	infile >> numCases;
	double ** cases	=  new double*[numCases];

	//cout << "numCases is " << numCases << endl;
	for (int i = 0 ; i < numCases; i++)
	{
		cases[i] = new double[3];
		for (int j = 0; j < 3; j++)
			infile >> cases[i][j];
	}
	*returnCases = cases;
	returnNumCases = numCases;
	//cout << "Done reading file\n";
}

double getTimeToBuyNFarms(double C, double F, double * timesToBuyNFarms, int N)
{
	if (timesToBuyNFarms[N] < 0)
	{
		if (N == 1)
			timesToBuyNFarms[N] = C / 2;
		else
			timesToBuyNFarms[N] = getTimeToBuyNFarms(C, F, timesToBuyNFarms, N-1) + C / (2+ (N-1)*F); 
	}
	return timesToBuyNFarms[N];
}

double getTimeToObtainXCookiesWithNFarms(double C, double F, double X, double * timesToBuyNFarms, double * timesToGetXCookiesWithNFarms, int N)
{
	if (timesToGetXCookiesWithNFarms[N] < 0)
	{
		if (N == 0)
			timesToGetXCookiesWithNFarms[N] = X / 2.0;
		else
			timesToGetXCookiesWithNFarms[N] = getTimeToBuyNFarms(C, F, timesToBuyNFarms, N) + X / (2 + N* F);
	}
	return timesToGetXCookiesWithNFarms[N];
}

double solveCase(double * iCase)
{

	double C = iCase[0];
	double F = iCase[1];
	double X = iCase[2];	
	//int Nmax = (int) X/F;
	int Nmax = (int) X * 1000;
	int N;
	double * timesToBuyNFarms = new double[Nmax+1]();
	double * timesToGetXCookiesWithNFarms = new double[Nmax+1]();
	double answer;
	for (int i = 0 ; i <= Nmax; i++)
	{
		timesToBuyNFarms[i] = -1.0;
		timesToGetXCookiesWithNFarms[i] = -1;
	}
	
	timesToBuyNFarms[0] = 0;  //I don't think this value will be used.
	for (int i = 0; i <= Nmax; i++)
		if (getTimeToObtainXCookiesWithNFarms(C, F, X, timesToBuyNFarms, timesToGetXCookiesWithNFarms, i) < getTimeToObtainXCookiesWithNFarms(C, F, X, timesToBuyNFarms, timesToGetXCookiesWithNFarms, i+1))
		{
			answer = getTimeToObtainXCookiesWithNFarms(C, F, X, timesToBuyNFarms, timesToGetXCookiesWithNFarms, i);  
			N = i;
			i = Nmax;
		}
/*
	cout << "for case: " << C << " " << F << " " << X << ", N is " << N << " and time is " << answer << endl;
	cout << "Nvalues were: " ;
	for (int i = 0; i <= N+1; i++)
		cout << getTimeToObtainXCookiesWithNFarms(C,F,X, timesToBuyNFarms, timesToGetXCookiesWithNFarms, i) << " " ;
	cout << endl;
*/
	delete []timesToBuyNFarms;
	delete []timesToGetXCookiesWithNFarms;
	return answer;
	
					
}


int solve(double ** cases, int numCases, double * solutions)
{
		//print_matrix(caseSizes, numCases, 2);
	//print_array(caseLengths, numCases);
	for (int i = 0; i < numCases; i++)  //outermost loop runs through each case
	{
		solutions[i] = solveCase(cases[i]);
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
	double ** cases;
	double * solutions;


	//cout << "hey" << endl;
	readfile(inpufile, &cases, numCases);
	//cout << "done reading file\n"; ;
	solutions = new  double[numCases]();
	solve(cases, numCases, solutions);
	for (int i = 0; i < numCases; i++)
	{
		//print_array_doubles(cases[i], 3);
		//cout << endl;
		//print_matrix(cases[i][1], 4, 4);
		//cout << endl;
		cout << "Case #" << i+1 << ": " << std::fixed << std::setprecision(9) << solutions[i] << endl;
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
