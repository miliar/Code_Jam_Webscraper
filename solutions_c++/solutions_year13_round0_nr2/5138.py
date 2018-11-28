// B. Lawnmower.cpp : 定义控制台应用程序的入口点。
//

#include <stdio.h>
#include <memory.h>

static char szResult[2][5] = {"YES", "NO"};

// 草坪数组
static int szDesLawn[100][100] = { 0 };

// 记录行列的最大值
static int szMaxRow[100];
static int szMaxCol[100];

// output Array
int szOutputArray[100] = { 0 };

// 判断草坪是否能够被割草机剪成目标模样
int JudgeIsLawmowerOk(int (*pDesLawn)[100][100], int nRows, int nCols, int* pMaxRow, int* pMaxCol)
{
	int nResult = 0; // 能够成功

	// 只要所在行，所在列都存在比它大的数值，则不可能
	for (int i = 0; i < nRows; i ++)
	{
		for (int j = 0; j < nCols; j ++)
		{
			// i行， j列 的最大值都比该元素e大， 即该行不能按照e剪， 该列不能按照e剪
			if ((*pDesLawn)[i][j] < pMaxRow[i] && (*pDesLawn)[i][j] < pMaxCol[j])
			{
				nResult = 1;
				return nResult;
			}
		}
	}

	return nResult;
}

int main()
{
	int nTimes, nRows, nCols, nTmp;
	int i, j , t;
	FILE* pFile = fopen("B-large.in", "r");

	// 输出次数
	fscanf(pFile, "%d\n", &nTimes);

	for (t = 0; t < nTimes; t ++)
	{
		fscanf(pFile, "%d %d\n", &nRows, &nCols);

		// 保存该行该列最大的值
		memset(szMaxRow, 0, sizeof(int) * nRows);
		memset(szMaxCol, 0, sizeof(int) * nCols);

		for (i = 0; i < nRows; i ++)
		{
			for (j = 0; j < nCols; j ++)
			{
				if (j == nCols - 1)
				{
					fscanf(pFile, "%d\n", &nTmp);
				}
				else
				{
					fscanf(pFile, "%d", &nTmp);
				}

				szDesLawn[i][j] = nTmp;

				// 找出第i行最大的 值
				if (szMaxRow[i] < nTmp)
				{
					szMaxRow[i] = nTmp;
				}

				// 找出第j列最大的值
				if(szMaxCol[j] < nTmp)
				{
					szMaxCol[j] = nTmp;
				}

			} // for j列
		} // for i 行

		szOutputArray[t] = JudgeIsLawmowerOk(&szDesLawn, nRows, nCols, szMaxRow, szMaxCol);
	}

	fclose(pFile);


	// OUTPUT
	pFile = fopen("output.txt", "w");
	for (t = 0; t < nTimes; t ++)
	{
		fprintf(pFile,"Case #%d: %s\n", t + 1, szResult[szOutputArray[t]]);
	}

	fclose(pFile);

	return 0;
}

