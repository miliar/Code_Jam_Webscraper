#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;
int main ()
{

	//Input
	uint numCases;
	cin>> numCases;

	int cardRow1, cardRow2;
	uint Cards1[4][4];
	uint Cards2[4][4];
	for(int i = 0; i < numCases;i++)
	{
		cin >> cardRow1;
		cardRow1--;

		for(int a = 0; a < 4; a ++)
		{
			for (int b = 0; b < 4; b ++)
			{
				cin >>Cards1[a][b];
			}
		}
		cin >> cardRow2;
		cardRow2--;

		for(int a = 0; a < 4; a ++)
		{
			for (int b = 0; b < 4; b ++)
			{
				cin >>Cards2[a][b];
			}
		}
		vector<int> matches;

		for (int x = 0; x < 4; x++)
		{
			for (int y = 0; y < 4; y++)
			{
				if(Cards1[cardRow1][y] == Cards2[cardRow2][x])
				{
					
					
						matches.push_back(Cards1[cardRow1][y]);	
			
					
				}
			}	
		}

	cout << "Case #" << i+1 << ": ";
		if(matches.size() ==1)
		{
			cout << matches.at(0);
		}else if( matches.size() == 0)
		{
			cout << "Volunteer cheated!";

		}else{
			cout << "Bad magician!" ;
		}
		cout << endl;





	}


	return 0;
}