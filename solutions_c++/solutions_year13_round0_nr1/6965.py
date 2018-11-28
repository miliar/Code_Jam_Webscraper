#include <cstdio>
#include <algorithm>
#include <vector>
#define SIZE 4
using namespace std;
char status[SIZE][SIZE];
int s; //0--DRAW, 1--NOT COMPLETE, 2--WON

char check(int a, int b, int c, int d)
{
	vector <char> tmp;
	if (status[a >> 2][a & 3] != 'T')
		tmp.push_back(status[a >> 2][a & 3]);
	if (status[b >> 2][b & 3] != 'T')
		tmp.push_back(status[b >> 2][b & 3]);
	if (status[c >> 2][c & 3] != 'T')
		tmp.push_back(status[c >> 2][c & 3]);
	if (status[d >> 2][d & 3] != 'T')
		tmp.push_back(status[d >> 2][d & 3]);
	sort(tmp.begin(), tmp.end());
	if (tmp[0] == '.')
		return '.';
	else
		if (tmp[0] == tmp[tmp.size() - 1])
				return tmp[0];
		else
				return 'A';

}

int main()
{
	int T;  
	char temp;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		s = 0;
		scanf("%c", &temp);
		for (int j = 0 ; j < SIZE; j++)
		{
			for (int k = 0; k < SIZE; k++)
				scanf("%c", &status[j][k]);
			scanf("%c", &temp);
		}
		for (int j = 0; j < SIZE; j++)
		{
			temp = check(j, j + SIZE, j + SIZE * 2, j + SIZE * 3);
			if (temp == '.')
				s = 1;
			else
				if (temp != 'A')
				{
					s = 2;
					break;
				}
		}
		if (s == 2)
		{
			printf("Case #%d: %c won\n", i, temp);
			continue;
		}
		for (int j = 0; j < SIZE * SIZE; j += SIZE)
		{
			temp = check(j, j + 1, j + 2, j + 3);
			if (temp == '.')
				s = 1;
			else
				if (temp != 'A')
				{
					s = 2;
					break;
				}
		}
		if (s == 2)
		{
			printf("Case #%d: %c won\n", i, temp);
			continue;
		}
		temp = check(0, 5, 10, 15);
		if (temp == '.')
			s = 1;
		else
			if (temp != 'A')
				s = 2;
		if (s == 2)
		{
			printf("Case #%d: %c won\n", i, temp);
			continue;
		}
		temp = check(3, 6, 9 ,12);
		if (temp == '.')
			s = 1;
		else
			if (temp != 'A')
				s = 2;
		if (s == 2)
			printf("Case #%d: %c won\n", i, temp);
		if (s == 1)
			printf("Case #%d: Game has not completed\n", i);
		if (s == 0)
			printf("Case #%d: Draw\n", i);
	}
return 0;
}
