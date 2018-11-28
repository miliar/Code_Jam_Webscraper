// adatt - C++ Solution to Magic Trick
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

int ansA, ansB, T, gridA[4][4], gridB[4][4], arrayA[4], arrayB[4];

int num_possible()
{
	int card = 0;
	int possibleCount = 0;
	
	for (int i=0; i < 4; i++)
	{
		arrayA[i] = gridA[ansA][i];
		arrayB[i] = gridB[ansB][i];
	}
	
	sort(arrayA, arrayA+4);
	sort(arrayB, arrayB+4);
	
//	for (int i=0; i < 4; i++)
//		cout << arrayA[i] << " " << arrayB[i] << "\n";
	
	for (int i=0; i < 4; i++) // run through both rows and check cards
	{
		for (int j=0; j < 4; j++)
			if (arrayA[i] == arrayB[j])
			{
				possibleCount++;
				card = arrayA[i];
			}
	}
	
	if (possibleCount == 0) // no possible cards for volunteer answer
		return -1;	
	else if (possibleCount > 1) // too many possibilities - magician is bad
		return 0;
	else
		return card;
}

int main()
{
	ofstream fout("magic.out");
	ifstream fin("magic.in");
	
	fin >> T;
	
	for (int prob=1; prob <= T; prob++)
	{
		fin >> ansA;
		for (int i=0; i < 4; i++)
			for (int j=0; j < 4; j++)
				fin >> gridA[i][j];
		
		fin >> ansB;
		for (int i=0; i < 4; i++)
			for (int j=0; j < 4; j++)
				fin >> gridB[i][j];
		
		ansA--; ansB--;		
		int temp = num_possible();
		
		if (temp == -1)
			fout << "Case #" << prob << ": Volunteer cheated!\n";
		else if (temp == 0)
			fout << "Case #" << prob << ": Bad magician!\n";
		else
			fout << "Case #" << prob << ": " <<  temp << "\n";
	}
	
	return 0;
}

