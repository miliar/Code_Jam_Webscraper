#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

pair<int, int> CompareCards(vector<int> c1, vector<int> c2);

int main(int argc, char **argv)
{
	int nCases, tmp;
	pair<int, int> response, result;
	pair<vector<int>, vector<int>> cards;
	ifstream inFile("A-small-attempt0.in");

	inFile >> nCases;
	cards.first = vector<int>(4);
	cards.second = vector<int>(4);

	for(int i=0; i<nCases; i++)
	{
		inFile >> response.first;

		for(int j=0; j<4; j++)
		{
			if( j == response.first-1 )
			{
				for(int k=0; k<4; k++)
					inFile >> cards.first[k];
			}
			else
			{
				for(int k=0; k<4; k++)
					inFile >> tmp;
			}
		}

		inFile >> response.second;
		for(int j=0; j<4; j++)
		{
			if( j == response.second-1 )
			{
				for(int k=0; k<4; k++)
					inFile >> cards.second[k];
			}
			else
			{
				for(int k=0; k<4; k++)
					inFile >> tmp;
			}
		}

		sort(cards.first.begin(), cards.first.end());
		sort(cards.second.begin(), cards.second.end());

		result = CompareCards(cards.first, cards.second);
		if( result.first == 1 )
			cout << "Case #" << i+1 << ": " << result.second << '\n';
		else if( result.first == 0 )
			cout << "Case #" << i+1 << ": Volunteer cheated!\n";
		else
			cout << "Case #" << i+1 << ": Bad magician!\n";
	}

	inFile.close();
	return 0;
}

pair<int, int> CompareCards(vector<int> c1, vector<int> c2)
{
	int count = 0, number;

	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if( c1[i] == c2[j] )
			{
				count++;
				number = c1[i];
			}
		}
	}

	return pair<int, int>(count, number);
}