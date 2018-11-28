#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

int main()
{ 
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int numCases;
	fin >> numCases;
	
	fout << setiosflags(ios::fixed) << setprecision(9);
	
	for (int caseNumber=1; caseNumber<=numCases; caseNumber++)
	{
		fout << "Case #" << caseNumber << ": ";
		
		int N;
		double V, X;
		fin >> N >> V >> X;
		
		double R[100], C[100], A[100];
		
		for (int i=0; i<N; i++)
			fin >> R[i] >> C[i];
			
		// case 1: only one source
		if (N == 1)
		{
			if (C[0] == X) 
				fout << V/R[0] << endl;
			else
				fout << "IMPOSSIBLE" << endl;
		}
		// case 2: two sources, but not invertible
		else if (C[0] == C[1])
		{
			if (C[0] == X) 
				fout << V/(R[0] + R[1]) << endl;
			else
				fout << "IMPOSSIBLE" << endl;
		}
		// case 3: two sources, invertible
		else
		{
			A[0] = V / R[0] * (C[1] - X) / (C[1] - C[0]); 
			A[1] = V / R[1] * (X - C[0]) / (C[1] - C[0]);
			
			if (A[0] < 0 || A[1] < 0)
				fout << "IMPOSSIBLE" << endl;
			else
				fout << max(A[0], A[1]) << endl;
		}
	}
 
    return 0;
}