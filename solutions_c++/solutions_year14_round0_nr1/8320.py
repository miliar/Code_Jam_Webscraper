// codejam201401.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include <iostream>
#include <tchar.h>

#define DECK_SIZE				4

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	short nTestcases;
	short nCurrentCase = 0;

	cin >> nTestcases;

	while (nCurrentCase++ < nTestcases)
	{
		short firstAnswer;
		short secondAnswer;
		short deck_cnt[DECK_SIZE*DECK_SIZE] = { 0 };
		short deck_first[DECK_SIZE][DECK_SIZE] = { 0 };
		short deck_second[DECK_SIZE][DECK_SIZE] = { 0 };

		cin >> firstAnswer;
		for (short i = 0; i < DECK_SIZE; i++)
		{
			for (short j = 0; j < DECK_SIZE; j++)
			{
				cin >> deck_first[i][j];;
				if (i == firstAnswer-1)
				{
					deck_cnt[deck_first[i][j]-1]++;
				}
			}
		}
		cin >> secondAnswer;
		for (short i = 0; i < DECK_SIZE; i++)
		{
			for (short j = 0; j < DECK_SIZE; j++)
			{
				cin >> deck_second[i][j];
				if (i == secondAnswer-1)
				{
					deck_cnt[deck_second[i][j]-1]++;
				}
			}
		}

		short result = 0;
		short cardNum = -1;
		for (short i = 0; i < (DECK_SIZE*DECK_SIZE); i++)
		{
			if (deck_cnt[i] == 2)
			{
				result++;
				cardNum = i + 1;
			}
		}

		cout << "Case #" << nCurrentCase << ": ";
		if (result == 1)
		{
			cout << cardNum;
		}
		else if (result <= 0)
		{
			cout << "Volunteer cheated!";
		}
		else
		{
			cout << "Bad magician!";
		}
		cout << endl;
	}


	return 0;
}

