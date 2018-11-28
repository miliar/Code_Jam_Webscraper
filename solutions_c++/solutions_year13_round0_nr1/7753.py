#include <stdlib.h>
#include <stdio.h>

#define SIZE 16

void check(int&, int&, int, int*);
void process(int&, int&, char, int&, int&);

int main()
{
	int n;
	char c = '\0';
	int winMasks[] = {	0xF000, 0x0F00, 0x00F0, 0x000F,
				0x8888, 0x4444, 0x2222, 0x1111,
				0x8421, 0x1248	};	

	scanf("%d", &n);
	scanf("%c", &c);

	for (int testNo = 0; testNo < n; testNo++)
	{
		int mask	= 0x01;
		int emptyCount	= 0;
		int xMask	= 0;
		int yMask	= 0;

		for (int charNo = 0; charNo < SIZE; charNo++)
		{
			scanf("%c", &c);
			
			process(xMask, yMask, c, mask, emptyCount);
		//	printf("Wczytano %d znak '%c' (mask = %d, empty = %d)\n", charNo, c, mask, emptyCount);
			
			if (charNo % 4 == 3) scanf("%c", &c);	
		}

		printf("Case #%d: ", testNo + 1);
		check(xMask, yMask, emptyCount, winMasks);
		printf("\n");

		scanf("%c", &c);
	}

	return 0;
}

void check(int& xMask, int& yMask, int emptyCount, int* winMasks)
{
	for (int i = 0; i < 10; i++)
	{
		if ((winMasks[i] & xMask) == winMasks[i])
		{
			printf("X won");
			return;
		}
		else if ((winMasks[i] & yMask) == winMasks[i])
		{
			printf("O won");
			return;
		}
	}

	if (emptyCount == 0)
	{
		printf("Draw");
		return;
	}

	printf("Game has not completed");
}

void process(int& xMask, int& yMask, char c, int& mask, int& emptyCount)
{
	switch (c)
	{
		case 'O':
			yMask |= mask;
			break;
		case 'X':
			xMask |= mask;
			break;
		case '.':
			emptyCount++;
			break;
		default:
			xMask |= mask;
			yMask |= mask;
	}

	mask <<= 1;
}
