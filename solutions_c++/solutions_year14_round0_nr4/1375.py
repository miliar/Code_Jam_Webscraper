#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

void main()
{
	ifstream inputFile("D-large.in");
	ofstream outputFile("output.txt");
	int T;
	int N;
	
	inputFile >> T;

	for(int i = 0; i < T; i++)
	{
		int DeceitScore = 0;
		int WarScore = 0;

		// Get info from input file
		inputFile >> N;
		vector<double> Naomi(N), Ken(N);
		
		for(int i = 0; i < N; i++)
			inputFile >> Naomi[i];
		for(int i = 0; i < N; i++)
			inputFile >> Ken[i];

		// Play with the info
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());

		vector<double> TempNaomi = Naomi, TempKen = Ken;
		while(!Naomi.empty())
		{
			if(Naomi.back() > Ken.back())
			{	
				Naomi.erase(--Naomi.end());
				Ken.erase(Ken.begin());
				WarScore++;
			}
			else
			{
				vector<double>::const_iterator it = Ken.begin();
				for(it; (*it) < Naomi.front(); it++);
				
				Naomi.erase(Naomi.begin());
				Ken.erase(it);
			}
		}

		Naomi = TempNaomi;
		Ken = TempKen;

		while(!Naomi.empty())
		{
			if(Naomi[0] < Ken[0])
			{
				Naomi.erase(Naomi.begin());
				Ken.erase(--Ken.end());
			}
			else
			{
				DeceitScore++;
				
				Naomi.erase(Naomi.begin());
				Ken.erase(Ken.begin());
			}
		}

		outputFile << "Case #" << i + 1 << ": " << DeceitScore << " " << WarScore;
		outputFile << endl;
	}

}
