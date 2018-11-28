#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <cstring>
#include <stack>
using namespace std;

#define x first
#define y second
#define pb push_back
#define mp make_pair

int n,t;
char field[10][10];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&t);
	for(int test = 0; test < t; test++)
	{
		scanf("%s\n",field[0]);
		scanf("%s\n",field[1]);
		scanf("%s\n",field[2]);
		scanf("%s\n",field[3]);
		scanf("\n");
		int state = -1;
		//Check X
		int c;
		int diag1 = 0;
		int diag2 = 0;
		for(int i = 0; i < 4; i++)
		{
			c = 0;
			for(int j = 0; j < 4; j++)
			{
				if ((field[i][j] == 'X')||(field[i][j] == 'T'))
					c++;
			}
			if (c == 4)
			{
				state = 1;
			}
			c = 0;
			for(int j = 0; j < 4; j++)
			{
				if ((field[j][i] == 'X')||(field[j][i] == 'T'))
					c++;
			}
			if (c == 4)
				state = 1;
			if ((field[i][i] == 'X')||(field[i][i] == 'T'))
				diag1++;
			if ((field[3-i][i] == 'X')||(field[3-i][i] == 'T'))
				diag2++;
		}
		if ((diag1 == 4)||(diag2 == 4))
			state = 1;
		//Check O
		if (state == -1)
		{
			diag1 = diag2 = 0;
			for(int i = 0; i < 4; i++)
			{
				c = 0;
				for(int j = 0; j < 4; j++)
				{
					if ((field[i][j] == 'O')||(field[i][j] == 'T'))
						c++;
				}
				if (c == 4)
					state = 2;
				c = 0;
				for(int j = 0; j < 4; j++)
				{
					if ((field[j][i] == 'O')||(field[j][i] == 'T'))
						c++;
				}
				if (c == 4)
					state = 2;
				if ((field[i][i] == 'O')||(field[i][i] == 'T'))
					diag1++;
				if ((field[3-i][i] == 'O')||(field[3-i][i] == 'T'))
					diag2++;
			}
			if ((diag1 == 4)||(diag2 == 4))
				state = 2;
		}
		if (state == -1)
		{
			for(int i = 0; i < 4; i++)
				for(int j = 0; j < 4; j++)
					if (field[i][j] == '.')
						state = 4;
		}
		if (state == -1)
			state = 3;
		switch(state)
		{
		case 1:
			printf("Case #%d: X won\n",test + 1);
			break;
		case 2:
			printf("Case #%d: O won\n",test + 1);
			break;
		case 3:
			printf("Case #%d: Draw\n",test + 1);
			break;
		case 4:
			printf("Case #%d: Game has not completed\n",test + 1);
			break;
		}
	}
	return(0);
}