#include <stdio.h>
#include <string.h>

#define X_WON        0
#define O_WON        1
#define NOT_COMPLETE 2
#define DRAW         3


bool checkWon(char _a[][4], int _x)
{
	int count;
	for (int i = 0; i < 4; ++i)
	{
		count = 0;
		for (int j = 0; j < 4; ++j)
		{
			if (_a[i][j] == _x || _a[i][j] == 'T')
				count++;
		}
		if (count == 4)
			return true;
	}

	for (int i = 0; i < 4; ++i)
	{
		count = 0;
		for (int j = 0; j < 4; ++j)
		{
			if (_a[j][i] == _x || _a[j][i] == 'T')
				count++;
		}
		if (count == 4)
			return true;
	}

	count = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (_a[i][i] == _x || _a[i][i] == 'T')
			count++;
	}
	if (count == 4)
		return true;

	count = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (_a[3-i][i] == _x || _a[3-i][i] == 'T')
			count++;
	}
	if (count == 4)
		return true;

	return false;
} // checkWon

int checkDots(char _a[][4])
{
	int count = 0;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
		{
			if (_a[i][j] == '.')
				count++;
		}
	return count;
}

int main()
{
    int num;
    scanf("%d\n", &num);

    for (int ii = 0; ii < num; ++ii)
    {
        char a[4][4];
        for (int i = 0; i < 4; ++i)
        {
            a[i][0] = getchar();
            a[i][1] = getchar();
            a[i][2] = getchar();
            a[i][3] = getchar();
            getchar();
        }
        getchar();

        int result = DRAW;
		if (checkWon(a, 'X'))
		{
			result = X_WON;
			goto print;
		}
		if (checkWon(a, 'O'))
		{
			result = O_WON;
			goto print;
		}
		if (checkDots(a) != 0)
		{
			result = NOT_COMPLETE;
			goto print;
		}

print:
        switch (result)
        {
            case X_WON:        { printf("Case #%d: X won\n", ii+1); break;                  }
            case O_WON:        { printf("Case #%d: O won\n", ii+1); break;                  }
            case DRAW:         { printf("Case #%d: Draw\n", ii+1); break;                   }
            case NOT_COMPLETE: { printf("Case #%d: Game has not completed\n", ii+1); break; }
        } // switch

    }

    return 0;
} // main
