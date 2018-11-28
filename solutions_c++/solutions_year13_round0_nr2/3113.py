// google jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string.h>
#include <math.h>
#include <stdlib.h>

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t=0;  //测试次数
	int M,N;
	bool result; //结果，初始化为真
	int lawn[100][100];//存储数据
	int rowMax[100],colMax[100]; //存储每行没咧的最大值
	scanf("%d",&T);  //获取测试次数
	while(t++<T)
	{
		//初始化数据区
		result = true;
		memset(rowMax,0,sizeof(rowMax));
		memset(colMax,0,sizeof(colMax));

		//获取矩形长宽
		scanf("%d",&N);
		scanf("%d",&M);

		//接收数据
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
				scanf("%d",&lawn[i][j]);

		//求每行每列的最大值
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
				rowMax[i] = rowMax[i]<lawn[i][j]?lawn[i][j]:rowMax[i];
		for(int i=0;i<M;++i)
			for(int j=0;j<N;++j)
				colMax[i] = colMax[i]<lawn[j][i]?lawn[j][i]:colMax[i];

		//判断是否成功
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

