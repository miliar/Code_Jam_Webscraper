#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<ctype.h>
#include<algorithm>
#include<queue>
#include<bitset>
#include<deque>
#include<set>
#include<math.h>
#include<functional>
#include<stack>
#include<map>
#include<vector>
#include<iostream>
#include<sstream>
#include <time.h> 
using namespace std;
#define LL long long 
char a[10][10];
void ok()
{
	char temp = '.';
	int cnt = 0;
	for(int i = 0; i < 4; i++)
	{
		temp = '.';
		if(a[i][0] == 'X')
			temp = 'X';
		if(a[i][0] == 'O')
			temp = 'O';
		if(a[i][0] == 'T')
		{
			if(a[i][1] == 'X')
				temp = 'X';
			if(a[i][1] == 'O')
				temp = 'O';
		}
		int j;
		if(temp != '.')
		{
			for(j = 1; j < 4; j++)
			{
				if(a[i][j]== temp || a[i][j] == 'T')
					continue;
				else
					break;
			}
			if(j == 4)
			{
				if(temp == 'X')
					printf("X won\n");
				else
					printf("O won\n");
				return;
			}
		}
	}

	for(int j = 0; j < 4; j++)
	{
		temp = '.';
		if(a[0][j] == 'X')
			temp = 'X';
		if(a[0][j] == 'O')
			temp = 'O';
		if(a[0][j] == 'T')
		{
			if(a[0][j] == 'X')
				temp = 'X';
			if(a[1][j] == 'O')
				temp = 'O';
		}
		int i;
		if(temp != '.')
		{
			for(i = 1; i < 4; i++)
			{
				if(a[i][j]== temp || a[i][j] == 'T')
					continue;
				else
					break;
			}
			if(i == 4)
			{
				if(temp == 'X')
					printf("X won\n");
				else
					printf("O won\n");

				return ;
			}
		}
	}
	temp = '.';
	if(a[0][0] == 'X')
		temp = 'X';
	if(a[0][0] == 'O')
		temp = 'O';
	if(a[0][0]== 'T')
	{
		if(a[1][1] == 'X')
			temp = 'X';
		if(a[1][1] == 'O')
			temp = 'O';
	}
	if(temp != '.')
	{
		int i;
		for( i = 1; i < 4; i++)
		{
			if(a[i][i] == temp || a[i][i] == 'T')
				continue;
			else
				break;
		}
		if(i == 4)
		{
			printf("%c won\n", temp);
			return ;
		}
	}

	temp = '.';
	if(a[0][3] == 'O')
		temp = 'O';
	if(a[0][3] == 'X')
		temp = 'X';
	if(a[0][3] == 'T')
	{
		if(a[1][2] == 'X')
			temp = 'X';
		if(a[1][2] == 'O')
			temp = 'O';
	}
	if(temp != '.')
	{
		int i, j = 1;
		for(i = 2; i >= 0; i--, j++)
		{
			if(a[j][i] == temp || a[j][i] == 'T')
				continue;
			else
				break;

		}
		if(i == -1)
		{
			printf("%c won\n", temp);
			return ;
		}
	}
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(a[i][j] == '.')
			{
				printf("Game has not completed\n");
				return ;
			}
		}
	}
	printf("Draw\n");
	return;

}
int main()
{
	int t, kk = 1;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	while(t--)
	{

		for(int i = 0; i < 4; i++)
			scanf("%s", a[i]);
		printf("Case #%d: ", kk++);
		ok();
	}
}
