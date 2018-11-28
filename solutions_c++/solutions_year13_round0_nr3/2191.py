#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ret[10000];
int rLen;
int A, B;

bool checkPalindrome(int data)
{
	char temp[20];
	itoa(data, temp, 10);
	
	int len = strlen(temp);
	int endIndex = len / 2;
	if ((len & 1) == 0)
	{
		-- endIndex;
	}
	
	for (int i = 0; i <= endIndex; ++ i)
	{
		if (temp[i] != temp[len - 1 - i])
		{
			return false;
		}
	}

	return true;
}

void prepare()
{
	rLen = 0;
	for (int i = 1; i * i <= 1000; ++ i)
	{
		if (checkPalindrome(i) && checkPalindrome(i * i))
		{
			//printf("%d %d\n", i, i * i);
			ret[rLen] = i * i;
			++ rLen;
		}
	}
}

void inputData()
{
	scanf("%d%d", &A, &B);
}

void process(int cases)
{
	int fromIndex = 0;
	for (; fromIndex < rLen; ++ fromIndex)
	{
		if (ret[fromIndex] >= A)
		{
			break;
		}
	}

	int endIndex = fromIndex;
	for (; endIndex < rLen; ++ endIndex)
	{
		if (ret[endIndex] > B)
		{
			break;
		}
	}

	printf("Case #%u: %u\n", cases, endIndex - fromIndex);
}

int main()
{
	//freopen("E:\\codejam\\C\\C-small-attempt0.in", "r", stdin);
	//freopen("E:\\codejam\\C\\out.txt", "w", stdout);
	prepare();

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++ i)
	{
		inputData();
		process(i);
	}
	return 0;
}