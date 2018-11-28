#include <iostream>
#include <string.h>
#include <cmath>
#include <stdio.h>

using namespace std;

int oper[][5] =
{
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};
int getNum(char c)
{
	switch(c)
	{
	case 'i':
		return 2;
	case 'j':
		return 3;
	default:
		return 4;
	}
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for(int iCase = 1; iCase <= T; iCase++)
	{
		int L, X;
		cin >> L >> X;
		static char str[10010], strTmp[10010];

		scanf("%s", str);
		strcpy(strTmp, str);
		for(int i=1;i<X;i++)
			strcat(str, strTmp);
		int sum = 1;
		int goal = 2;
		for(int i = 0; i < L*X; i++)
		{
			int now = getNum(str[i]);
			sum = (sum > 0 ? 1 : -1) * oper[sum>0?sum:-sum][now];
			if(sum == goal && goal!=4)
			{
				goal++;
				sum = 1;
			}
		}
		printf("Case #%d: %s\n", iCase, sum == 4 && goal == 4 ? "YES" : "NO");
	}

	return 0;
}
