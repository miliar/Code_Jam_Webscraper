// google jam.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <string.h>
#include <math.h>
#include <stdlib.h>

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t=0;  //���Դ���
	int M,N;
	bool result; //�������ʼ��Ϊ��
	int lawn[100][100];//�洢����
	int rowMax[100],colMax[100]; //�洢ÿ��û�ֵ����ֵ
	scanf("%d",&T);  //��ȡ���Դ���
	while(t++<T)
	{
		//��ʼ��������
		result = true;
		memset(rowMax,0,sizeof(rowMax));
		memset(colMax,0,sizeof(colMax));

		//��ȡ���γ���
		scanf("%d",&N);
		scanf("%d",&M);

		//��������
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
				scanf("%d",&lawn[i][j]);

		//��ÿ��ÿ�е����ֵ
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
				rowMax[i] = rowMax[i]<lawn[i][j]?lawn[i][j]:rowMax[i];
		for(int i=0;i<M;++i)
			for(int j=0;j<N;++j)
				colMax[i] = colMax[i]<lawn[j][i]?lawn[j][i]:colMax[i];

		//�ж��Ƿ�ɹ�
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
				if(lawn[i][j] < rowMax[i] && lawn[i][j] < colMax[j])
				{
					result = false;
					goto R;
				}
R:		if(result)
		{
			printf("Case #%d: YES\n",t);
		}
		else
		{
			printf("Case #%d: NO\n",t);
		}
	}
	return 0;
}

