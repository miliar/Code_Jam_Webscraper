#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{ 
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int numCases;
	fin >> numCases;
	
	for (int caseNumber=1; caseNumber<=numCases; caseNumber++)
	{
		fout << "Case #" << caseNumber << ": ";
		
		int N;
		fin >> N;
		
		int numHiker = 0;
		long D[10], M[10];
		
		for (int i=0; i<N; i++)
		{
			long d, h, m;
			fin >> d >> h >> m;
			for (int j=0; j<h; j++)
			{
				D[numHiker] = d;
				M[numHiker] = m + j;
				
				numHiker++;
			}
		}
		
		int f = 0;
		for (int i=1; i<numHiker; i++)
			if (M[i] < M[f])
				f = i;
		
		int count = 0;
		for (int i=0; i<numHiker; i++)
		{
			if (i==f) continue;
		
			if (M[f] * (720 - D[f]) <= M[i] * (360 - D[i]))
				count++;
			//else if (M[i] * (720 - D[f]) >= M[f] * (720 - D[i]))
			//	count++;
		}
		fout << count << endl;
	}
 
    return 0;
}