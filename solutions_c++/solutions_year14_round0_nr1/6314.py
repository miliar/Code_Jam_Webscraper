// Magic Trick.cpp : 定义控制台应用程序的入口点。
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
using namespace std;


int main(int argc, char* argv[])
{	
	FILE* fp;
	freopen_s(&fp, "A-small-attempt0.in", "r", stdin );
	freopen_s(&fp, "A-small-practice.out", "w", stdout );

	int n;

	cin >> n;
	
	for(int caseN = 1; caseN <= n; ++caseN)
	{
		int row1;
		cin >> row1;

		int cards[4][4];
		for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; j++) cin >> cards[i][j];

		int row2;
		cin >> row2;

		int cards2[4][4];
		for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; j++) cin >> cards2[i][j];

		int chosenCard = 0;
		bool bMulti = false;
		for(int i = 0; i < 4; i++)
		{
			int card = cards2[row2-1][i];
			for(int j = 0; j < 4; ++j)
			{
				if(cards[row1-1][j] == card)
				{
					if(0 == chosenCard)
					chosenCard = card;
					else
					bMulti = true;

					break;
				}
			}

			if( bMulti ) break;
		}
		
		if( bMulti )
			printf_s("Case #%d: %s\n", caseN, "Bad magician!" );
		else if( chosenCard )
			printf_s("Case #%d: %d\n", caseN, chosenCard );
		else
			printf_s("Case #%d: %s\n", caseN, "Volunteer cheated!" );
	}

	return 0;
}

