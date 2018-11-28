// reading a text file
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <climits>

using namespace std;

int main () {
	// define variables
	int numTC;
	int K, C, S;

	ifstream myfile ("D-small-attempt1.in");
	ofstream savefile ("D-small-attempt1.out");
	
	if(!myfile.is_open())
		cout << "File not found";

	myfile >> numTC;

	for(int t = 0; t < numTC; t++) // run each test case
	{	
		myfile >> K;
		myfile >> C;
		myfile >> S;
		
		int numGrads = 0;
		
		long long int* lookingPos = new long long int[2*K];

		if(C == 1)
		{
			for(int i = 1; i <= K; i = i + 1) // accessing block i
			{
				lookingPos[numGrads] = i;
				// cout << i << " ";
				numGrads++;
			}
				
		}
		else
		{
			for(int i = 1; i <= K; i = i+2) // accessing block i
			{
				int posInBlock = i + 1;
				if(posInBlock > K)
					posInBlock = K;
				
				long long int pickPos = (i - 1) * pow(K, C-1) + posInBlock;
				
				// cout << pickPos << " ";
				lookingPos[numGrads] = pickPos;
				numGrads++;
			}
		}
		
		savefile << "Case #" << (t + 1) << ": ";
		
		/* if(S < numGrads)
			savefile << "IMPOSSIBLE";
		else
		{
			for(int i = 0; i < numGrads; i = i + 1) // accessing block i
			{
				savefile << lookingPos[i] << " ";
			}
		} */
		
		for(int i = 0; i < S; i = i + 1) // accessing block i
		{
			savefile << i + 1 << " ";
		}

		savefile << endl;
	}

	myfile.close();
	savefile.close();

	return 0;
}


