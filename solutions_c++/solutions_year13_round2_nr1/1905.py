#include <stdio.h>
#include <vector>
#include <algorithm>

int A, N, operation;
std::vector<int> mote;

bool compare(int a, int b)
{
	return a < b;
}

void chk(int i, int operationNumber)
{
	//printf("%d %d %d %d\n", i, A, mote[i], operationNumber);
	if (i == N)
	{
		if (operation > operationNumber)
		{
			operation = operationNumber;
		}
		return;
	}
	if (A > mote[i])
	{
		A += mote[i];
	}
	else
	{
		if (operation > operationNumber + N - i)
		{
			operation = operationNumber + N - i;
		}
		while (mote[i] >= A)
		{
			A += A - 1;
			operationNumber++;
		}
		A += mote[i];
	}
	chk(i + 1, operationNumber);
}

int main()
{
	int testN;
	scanf_s("%d", &testN);
	for (int testNumber = 1; testNumber <= testN; testNumber++)
	{
		mote.clear();
		operation = 999;
		
		scanf_s("%d%d", &A, &N);
		for (int i = 0; i < N; i++)
		{
			int tem;
			scanf_s("%d", &tem);
			mote.push_back(tem);
		}

		sort(mote.begin(), mote.end(), compare);

		if (A == 1)
		{
			operation = N;
		}
		else
		{
			chk(0, 0);
		}

		printf("Case #%d: %d\n", testNumber, operation);
	}
}