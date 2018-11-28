/*

 *
 */


#include <iostream>
#include <fstream>
#include <algorithm>
#include <stack>



using namespace std;


int main()
{
	ifstream inf;
	ofstream outf;
	inf.open("B-large.in", ios::in);
	outf.open("output.txt");


	int T;
	int N, M;
	int x, max= 0;
	int* MaxCols, *MinCols;		// row vector
	int* MaxRows, *MinRows;		// column vector
	int** arr;
	string line;
	
	
	inf >> T;
	for(int k = 0; k < T; k++)
	{
		bool result = true;
		
		inf >> N;
		inf >> M;
		
		MaxRows = new int[N];
		MaxCols = new int[M];
		MinRows = new int[N];
		MinCols = new int[M];
		for(int i = 0; i < N; i++) MaxRows[i] = 0;
		for(int i = 0; i < M; i++) MaxCols[i] = 0;
		for(int i = 0; i < N; i++) MinRows[i] = 0;
		for(int i = 0; i < M; i++) MinCols[i] = 0;
		
		arr = new int*[N];
		for(int i = 0; i < N; i++) arr[i] = new int[M];
		
		// get one test case
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < M; j++) {
				inf >> x;
				if(x > MaxRows[i])	MaxRows[i] = x;
				if(x > MaxCols[j])	MaxCols[j] = x;
				if(x < MinRows[i])	MinRows[i] = x;
				if(x < MinCols[j])	MinCols[j] = x;
				
				arr[i][j] = x;
			}
		}
		
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < M; j++) {
				if(arr[i][j] < MaxCols[j] && arr[i][j] < MaxRows[i]) {
					j = M;
					i = N;
					result = false;
				}
			}
		}
		
		delete[] MaxRows;
		delete[] MaxCols;
		for(int i = 0; i < N; i++) delete[] arr[i];
		delete[] arr;
		// finish getting one test case
		

		outf << "Case #" << (k+1) << ": ";
		
		if(result)
			outf << "YES";
		else
			outf << "NO";
	
		outf << endl;
		
		
	}


	inf.close();
	outf.close();
	return 0;
}
