// CodeJam2016.cpp : ��`��T���p�����I�i���y�B
//

#include "stdafx.h"
#include "string.h"

void ProblemB()
{
	int nTurns = 0;
	scanf_s("%d\n",&nTurns);
	for (int x=0;x<nTurns;x++)
	{
		char string[201];
		int nCount = 0; // answer
		fgets(string, 201, stdin);
		char finalC = string[strlen(string)-1];
		if (finalC != '-' && finalC != '+')
			string[strlen(string)-1] = 0;
		char cur = ' ';
		for (int i=0;i<strlen(string);i++)
		{
			if (cur != ' ')
			{
				if (cur != string[i])
				{
					nCount++;
					//printf("switch:cur:%c string[%d]:%c\n",cur,i,string[i]);
				}
			}
			cur = string[i];
		}
		if (cur == '-')
			nCount++;
		printf("Case #%d: %d\n",x+1, nCount);
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ProblemB();
	return 0;
}

