// B. Lawnmower.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include <stdio.h>
#include <memory.h>

static char szResult[2][5] = {"YES", "NO"};

// ��ƺ����
static int szDesLawn[100][100] = { 0 };

// ��¼���е����ֵ
static int szMaxRow[100];
static int szMaxCol[100];

// output Array
int szOutputArray[100] = { 0 };

// �жϲ�ƺ�Ƿ��ܹ�����ݻ�����Ŀ��ģ��
int JudgeIsLawmowerOk(int (*pDesLawn)[100][100], int nRows, int nCols, int* pMaxRow, int* pMaxCol)
{
	int nResult = 0; // �ܹ��ɹ�

	// ֻҪ�����У������ж����ڱ��������ֵ���򲻿���
	for (int i = 0; i < nRows; i ++)
	{
		for (int j = 0; j < nCols; j ++)
		{
			// i�У� j�� �����ֵ���ȸ�Ԫ��e�� �����в��ܰ���e���� ���в��ܰ���e��
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

	// �������
	fscanf(pFile, "%d\n", &nTimes);

	for (t = 0; t < nTimes; t ++)
	{
		fscanf(pFile, "%d %d\n", &nRows, &nCols);

		// ������и�������ֵ
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

				// �ҳ���i������ ֵ
				if (szMaxRow[i] < nTmp)
				{
					szMaxRow[i] = nTmp;
				}

				// �ҳ���j������ֵ
				if(szMaxCol[j] < nTmp)
				{
					szMaxCol[j] = nTmp;
				}

			} // for j��
		} // for i ��

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

