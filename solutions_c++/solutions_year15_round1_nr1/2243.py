//Code Jam round 1A
//Mushroom Monster

#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
	int t, n;

	ifstream fin;
	ofstream fout;

	fin.open("A-large.in");
	fout.open("output.txt");

	fin >> t;

	for (int i = 1; i <= t; i++)
	{
		fin >> n;
		
		int min1 = 0;
		int min2 = 0;
		int maxDif = 0;

		int * mushArray = new int[n];
		int * diffArray = new int[n - 1];


		for (int j = 0; j < n; j++)
			fin >> mushArray[j];

		for (int j = 0; j < (n - 1); j++)
			diffArray[j] = mushArray[j] - mushArray[j + 1];

		for (int j = 0; j < (n - 1); j++)		//find maximum difference = constant rate
		{
			if (diffArray[j] > maxDif)
				maxDif = diffArray[j];
		}

		for (int j = 0; j < (n - 1); j++)
		{
			if (diffArray[j] >= 0)
				min1 += diffArray[j];		//if some must be eaten, add that amount

			if (mushArray[j] >= maxDif)
				min2 += maxDif;
			else
				min2 += mushArray[j];
		}

		fout << "Case #" << i << ": " << min1 << " " << min2 << endl;
	}


	return 0;
}