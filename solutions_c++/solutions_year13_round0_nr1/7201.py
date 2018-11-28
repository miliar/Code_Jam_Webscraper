#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

using namespace std;

unsigned char b[4][4];

int checkWinner()
{
	int x, y, mc;

	for (x=0;x<4;x++)
	{
		mc = 0;

		for (y=0;y<4;y++)
		{
			if (b[x][y] == 'X' || b[x][y] == 'T')
				mc++;
			else
				break;
		}

		if (mc == 4)
		{
			return (1);
		}
	}

	for (y=0;y<4;y++)
	{
		mc = 0;

		for (x=0;x<4;x++)
		{
			if (b[x][y] == 'X' || b[x][y] == 'T')
				mc++;
			else
				break;
		}

		if (mc == 4)
		{
			return (1);
		}
	}

	mc = 0;

	for (x=0,y=0;x<4&&y<4;x++,y++)
	{
		if (b[x][y] == 'X' || b[x][y] == 'T')
			mc++;
		else
			break;
	}

	if (mc == 4)
	{
		return (1);
	}


	mc = 0;

	for (x=3,y=0;x>=0&&y<4;x--,y++)
	{
		if (b[x][y] == 'X' || b[x][y] == 'T')
			mc++;
		else
			break;
	}

	if (mc == 4)
	{
		return (1);
	}

	for (x=0;x<4;x++)
	{
		mc = 0;

		for (y=0;y<4;y++)
		{
			if (b[x][y] == 'O' || b[x][y] == 'T')
				mc++;
			else
				break;
		}

		if (mc == 4)
		{
			return (2);
		}
	}

	for (y=0;y<4;y++)
	{
		mc = 0;

		for (x=0;x<4;x++)
		{
			if (b[x][y] == 'O' || b[x][y] == 'T')
				mc++;
			else
				break;
		}

		if (mc == 4)
		{
			return (2);
		}
	}

	mc = 0;

	for (x=0,y=0;x<4&&y<4;x++,y++)
	{
		if (b[x][y] == 'O' || b[x][y] == 'T')
			mc++;
		else
			break;
	}

	if (mc == 4)
	{
		return (2);
	}

	mc = 0;

	for (x=3,y=0;x>=0&&y<4;x--,y++)
	{
		if (b[x][y] == 'O' || b[x][y] == 'T')
			mc++;
		else
			break;
	}

	if (mc == 4)
	{
		return (2);
	}

	for (x=0;x<4;x++)
	{
		for (y=0;y<4;y++)
		{
			if (b[x][y] == '.')
			{
				return (0);
			}
		}
	}

	return (3);
}

int main(int argc, char *argv[])
{
	FILE *fp;
	char buff[1024];
	int i;
	int ci;
	int numOfCase;
	int r;

	fp = fopen(argv[1], "r");

	if (!fp) return (-1);

	numOfCase = atoi(fgets(buff, sizeof(buff), fp));
	for(ci=1;ci<=numOfCase;ci++)
	{
		for (i=0;i<4;i++)
		{
			fgets(buff, sizeof(buff), fp);
			sscanf(buff, "%c%c%c%c", &b[i][0], &b[i][1], &b[i][2], &b[i][3]);
		}

		fgets(buff, sizeof(buff), fp); // read empty line

		/* DEBUG PRINT
		for (x=0;x<4;x++)
		{
			for (y=0;y<4;y++)
			{
				printf("%c", b[x][y]);
			}
			cout << endl;
		}
		cout << "==================================" << endl;
		*/

		r = checkWinner();

		if (r==1)
			cout << "Case #" << ci << ": X won" << endl;
		else if (r==2)
			cout << "Case #" << ci << ": O won" << endl;
		else if (r==3)
			cout << "Case #" << ci << ": Draw" << endl;
		else if (r==0)
			cout << "Case #" << ci << ": Game has not completed" << endl;
	}
	
	fclose(fp);
	return (0);
}

