/*
* File:   main.cpp
* Author: Sreekanth
*
* Created on May 21, 2011
*/

#include "stdlib.h"
#include "stdio.h"

int main()
{
	freopen("I.in","r",stdin);
	freopen("O.op","w",stdout);

	int cases;
	scanf("%d",&cases);
	int caserunning=0;
	while (cases--)
	{
		char elems[4][4] = {0};
		bool tfound = false;
		bool crap = false;
		for(int i = 0; i < 4; i++)
		{
			char dummy;
			scanf("%c",&dummy);
			for(int j = 0 ; j < 4 ; j++)
			{
				scanf("%c",&elems[i][j]);
				if(elems[i][j] == 'T')
				{
					if(!tfound)
					{
						tfound = true;
					}
					else
					{
						crap = true;
					}
				}
			}
		}

	/*	if(crap || !tfound)
		{
			printf("Case #%d: Game has not completed\n" , ++caserunning);
		}
*/
		if( ((elems[0][0] == 'X' || elems[0][0] == 'T') &&
				(elems[0][1] == 'X' || elems[0][1] == 'T') &&
				(elems[0][2] == 'X' || elems[0][2] == 'T') &&
				(elems[0][3] == 'X' || elems[0][3] == 'T')) ||
				((elems[1][0] == 'X' || elems[1][0] == 'T') &&
				(elems[1][1] == 'X' || elems[1][1] == 'T') &&
				(elems[1][2] == 'X' || elems[1][2] == 'T') &&
				(elems[1][3] == 'X' || elems[1][3] == 'T')) ||
				((elems[2][0] == 'X' || elems[2][0] == 'T') &&
				(elems[2][1] == 'X' || elems[2][1] == 'T') &&
				(elems[2][2] == 'X' || elems[2][2] == 'T') &&
				(elems[2][3] == 'X' || elems[2][3] == 'T')) ||
				((elems[3][0] == 'X' || elems[3][0] == 'T') &&
				(elems[3][1] == 'X' || elems[3][1] == 'T') &&
				(elems[3][2] == 'X' || elems[3][2] == 'T') &&
				(elems[3][3] == 'X' || elems[3][3] == 'T')) ||
				((elems[0][0] == 'X' || elems[0][0] == 'T') &&
				(elems[1][1] == 'X' || elems[1][1] == 'T') &&
				(elems[2][2] == 'X' || elems[2][2] == 'T') &&
				(elems[3][3] == 'X' || elems[3][3] == 'T')) ||
				((elems[0][3] == 'X' || elems[0][3] == 'T') &&
				(elems[1][2] == 'X' || elems[1][2] == 'T') &&
				(elems[2][1] == 'X' || elems[2][1] == 'T') &&
				(elems[3][0] == 'X' || elems[3][0] == 'T'))
				)
		{
			printf("Case #%d: X won\n" , ++caserunning);
		}
		else if( ((elems[0][0] == 'O' || elems[0][0] == 'T') &&
				(elems[0][1] == 'O' || elems[0][1] == 'T') &&
				(elems[0][2] == 'O' || elems[0][2] == 'T') &&
				(elems[0][3] == 'O' || elems[0][3] == 'T')) ||
				((elems[1][0] == 'O' || elems[1][0] == 'T') &&
				(elems[1][1] == 'O' || elems[1][1] == 'T') &&
				(elems[1][2] == 'O' || elems[1][2] == 'T') &&
				(elems[1][3] == 'O' || elems[1][3] == 'T')) ||
				((elems[2][0] == 'O' || elems[2][0] == 'T') &&
				(elems[2][1] == 'O' || elems[2][1] == 'T') &&
				(elems[2][2] == 'O' || elems[2][2] == 'T') &&
				(elems[2][3] == 'O' || elems[2][3] == 'T')) ||
				((elems[3][0] == 'O' || elems[3][0] == 'T') &&
				(elems[3][1] == 'O' || elems[3][1] == 'T') &&
				(elems[3][2] == 'O' || elems[3][2] == 'T') &&
				(elems[3][3] == 'O' || elems[3][3] == 'T')) ||
				((elems[0][0] == 'O' || elems[0][0] == 'T') &&
				(elems[1][1] == 'O' || elems[1][1] == 'T') &&
				(elems[2][2] == 'O' || elems[2][2] == 'T') &&
				(elems[3][3] == 'O' || elems[3][3] == 'T')) ||
				((elems[0][3] == 'O' || elems[0][3] == 'T') &&
				(elems[1][2] == 'O' || elems[1][2] == 'T') &&
				(elems[2][1] == 'O' || elems[2][1] == 'T') &&
				(elems[3][0] == 'O' || elems[3][0] == 'T'))
				)
		{
			printf("Case #%d: O won\n" ,++caserunning);
		}
		else
		{
			bool incomplete = false;
			for(int i = 0; i < 4; i++)
			{
				for(int j = 0 ; j < 4 ; j++)
				{
					if(elems[i][j] == '.')
					{
						incomplete = true;
						break;
					}
				}
				if(incomplete)
				{
					break;
				}
			}
			if(incomplete)
			{
				printf("Case #%d: Game has not completed\n" , ++caserunning);
			}
			else
			{
				printf("Case #%d: Draw\n" , ++caserunning);
			}
		}
		char dummy;
		scanf("%c",&dummy);

	}


	return 0;
}
