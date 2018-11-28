
#include <iostream>

using namespace std;

bool IsFairNum(int num)
{
	char str[20];
	sprintf(str, "%d", num);
	int str_len = strlen(str);

	for (int i = 0; i < str_len / 2; i++)
	{
		if (str[i] != str[str_len-1-i])
			return false;
	}
	return true;
}

int main(int argc, char *argv[])
{
	int i, j, nCaseCnt;
	char  arrFairSquare[1024] = {0};

	arrFairSquare[1] = true;
	for (i = 2; i <= 1000; i++)
	{
		int num = i;

		bool bIsFair = IsFairNum(num);
		while (bIsFair)
		{
			num *= num;
			if (num <= 1000)
			{
				bIsFair = IsFairNum(num);
				if (bIsFair)
					arrFairSquare[num] = true;
			}
			else
				break;
		}
	}

	cin >> nCaseCnt;
	for (i = 0; i < nCaseCnt; i++)
	{
		int a, b, nFairSqure = 0;
		cin >> a >> b;
		for (j = a; j <= b; j++)
			if (arrFairSquare[j])
				nFairSqure++;
		printf("Case #%d: %d\n", i+1, nFairSqure);
	}

	return 0;
}
