#include <iostream>
#include <stdlib.h>
using namespace std;

float block1[1000];
float block2[1000];

int compare (const void * a, const void * b)
{
	float c = ( *((float*)a) - *((float*)b) );
	if (c > 0) return 1;
	else if (c < 0) return -1;
	else return 0;
}

int main()
{
	int nCase = 0;
	cin >> nCase;

	for (int i=0; i<nCase; i++)
	{
		int nBlocks = 0;
		cin >> nBlocks;

		for (int j=0; j<nBlocks; j++)
		{
			cin >> block1[j];			
		}

		for (int j=0; j<nBlocks; j++)
		{
			cin >> block2[j];
		}

		qsort(block1, nBlocks, sizeof(float), compare);
		qsort(block2, nBlocks, sizeof(float), compare);
		
		// play war
		int m = 0, n = 0;
		int score = 0;
			
		while(m < nBlocks) 
		{
			while(n < nBlocks && block1[m] > block2[n])
			{
				n++;
			}
			if (n == nBlocks) //block1�е�ǰ���block2���������, ��ô����ķֶ���block1��
			{
				score += (nBlocks - m);
				break;
			}
			else //block2�÷֣������ƽ�һ��
			{
				m++;
				n++;
			}
		}
		int res1 = score;

		// play deceitful war
		m = 0, n = 0;
		score = 0;

		while(m < nBlocks)
		{
			if (block1[m] < block2[n])
			{
				m++; // ����һ��αװһ�£�������block2�������
			}
			else
			{
				m++;
				n++;
				score++; //������αװһ�£�������block2����С��
			}
		}

		int res2 =score;

		printf("Case #%d: %d %d\n", i+1, res2, res1);
	}
	return 0;
}