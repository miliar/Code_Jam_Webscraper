#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

int m[102][102];
int N,M;

bool Success()
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
		{
			int h = m[i][j];
			//�����κ�һ���������ĺ��������������һ����ȫ���������ߵ�
			
			bool sucRaw = true;
			//�к���
			for(int k=0;k<M;k++)
			{
				if(m[i][k]>h)
					sucRaw = false;
			}
			bool sucCol = true;
			//�к���
			for(int k=0;k<N;k++)
			{
				if(m[k][j]>h)
					sucCol = false;
			}
			if(!sucRaw && !sucCol)
				return false;
		}
	}
	return true;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int kcase = 1; kcase <=T; kcase++)
	{
		scanf("%d%d",&N,&M);
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				scanf("%d", &m[i][j]);
			}
		}
		if(Success())
		{
			printf("Case #%d: YES\n", kcase);
		}
		else
		{
			printf("Case #%d: NO\n", kcase);
		}
	}
}
