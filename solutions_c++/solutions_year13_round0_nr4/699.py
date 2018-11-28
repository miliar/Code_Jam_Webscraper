#include <stdio.h>
#include <string.h>

const int maxKeyNum = 406;
const int maxChest = 206;

int K, N;
int keyNum[maxKeyNum];
int totalKeyNum[maxKeyNum];

int chestIdToKeyId[maxChest];
int keyInChest[maxChest][maxKeyNum];
int keyNumInChest[maxChest];

int maxKeyIndex;

bool searchedChest[maxChest];
bool keyIdFromChestId[maxKeyNum][maxChest];
int result[maxChest];

void inputData()
{
	scanf("%d%d", &K, &N);
	
	memset(keyNum, 0, sizeof(keyNum));
	memset(totalKeyNum, 0, sizeof(totalKeyNum));
	memset(keyIdFromChestId, 0, sizeof(keyIdFromChestId));

	int keyId;
	for (int i = 0; i < K; ++ i)
	{
		scanf("%d", &keyId);
		++ keyNum[keyId];
		++ totalKeyNum[keyId];
	}
	
	for (int i = 1; i <= N; ++ i)
	{
		scanf("%d%d", &chestIdToKeyId[i], &keyNumInChest[i]);
		-- totalKeyNum[chestIdToKeyId[i]];

		for (int j = 0; j < keyNumInChest[i]; ++ j)
		{
			scanf("%d", &keyInChest[i][j]);
			++ totalKeyNum[keyInChest[i][j]];
			if (keyInChest[i][j] != chestIdToKeyId[i])
			{
				keyIdFromChestId[keyInChest[i][j]][i] = true;
			}
		}
	}
}

bool searchResult(int d)
{
	if (d == N)
	{
		return true;
	}

	for (int i = 1; i <= N; ++ i)
	{
		if (searchedChest[i])
		{
			continue;
		}

		int keyType = chestIdToKeyId[i];
		if (keyNum[keyType] <= 0)
		{
			continue;
		}
		
		searchedChest[i] = true;

		-- keyNum[keyType];
		for (int j = 0; j < keyNumInChest[i]; ++ j)
		{
			++ keyNum[keyInChest[i][j]];
		}
		
		result[d] = i;
		if (keyNum[keyType] == 0)
		{
			bool bDepend = false;
			bool bRemain = false;
			for (int j = 1; j <= N; ++ j)
			{
				if (searchedChest[j])
				{
					continue;
				}

				if (chestIdToKeyId[j] == keyType)
				{
					bDepend = true;
				}

				if (keyIdFromChestId[keyType][j])
				{
					bRemain = true;
				}
			}

			if (bDepend && !bRemain)
			{
				searchedChest[i] = false;
				++ keyNum[keyType];

				for (int j = 0; j < keyNumInChest[i]; ++ j)
				{
					-- keyNum[keyInChest[i][j]];
				}
				continue;
			}
		}

		if (searchResult(d + 1))
		{
			return true;
		}
		
		searchedChest[i] = false;
		++ keyNum[keyType];
		
		for (int j = 0; j < keyNumInChest[i]; ++ j)
		{
			-- keyNum[keyInChest[i][j]];
		}
	}
	return false;
}

bool checkNoAnswer()
{
	for (int i = 1; i <= N; ++ i)
	{
		if (totalKeyNum[chestIdToKeyId[i]] < 0)
		{
			return true;
		}
	}

	return false;
}

void process(int cases)
{
	for (int i = 1; i <= N; ++ i)
	{
		searchedChest[i] = false;
	}
	
	printf("Case #%d: ", cases);
	if (checkNoAnswer())
	{
		printf("IMPOSSIBLE\n");
		return;
	}

	if (searchResult(0))
	{
		for (int i = 0; i < N; ++ i)
		{
			if (i < N - 1)
			{
				printf("%d ", result[i]);
			}
			else
			{
				printf("%d\n", result[i]);
			}
		}
	}
	else
	{
		printf("IMPOSSIBLE\n");
	}
}

int main()
{
	//freopen("E:\\codejam\\D\\D-small-attempt3.in", "r", stdin);
	//freopen("E:\\codejam\\D\\out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++ i)
	{
		inputData();
		process(i);
	}
	return 0;
}

/*
200
2 20
1 2
2 1 2
3 1 3
2 0
1 3 2 3 3
3 3 3 1 1
2 3 3 1 2
2 0
3 1 3
2 0
1 2 3 3
1 1 3
2 0
1 0
2 0
3 0
1 3 2 2 2
3 0
3 4 3 2 1 2
2 0
1 1 2

10 20
1 2 3 4 5 6 7 8 9 10
5 0
6 0
4 1 4
2 0
8 1 8
1 0
10 0
1 1 1
10 1 10
6 1 6
9 1 9
2 1 2
8 0
9 0
7 1 7
3 1 3
3 0
7 0
5 1 5
4 0
*/