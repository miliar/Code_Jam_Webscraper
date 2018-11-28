// google_2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{

	int lawn[100][100];
	int row[100];
	int col[100];
	int N,M,T;
	char a;
	bool flag;
	FILE *fin;
	FILE *fout;
	fin=fopen("B-large.in","r");
	if(fin==NULL)
		printf("input file open error!\n");
	fout=fopen("B-large.out","w");
	if(fout==NULL)
		printf("output file open error!\n");
	fscanf(fin,"%d",&T);
	fscanf(fin,"%c",&a);
	for (int t=1;t<=T;t++)
	{
		fscanf(fin,"%d",&N);
		fscanf(fin,"%c",&a);
		fscanf(fin,"%d",&M);
		fscanf(fin,"%c",&a);
		
		for (int n=0;n<N;n++)
		{
			for(int m=0;m<M;m++)
			{
					fscanf(fin,"%d",&lawn[n][m]);
					fscanf(fin,"%c",&a);
			
			}
		
		}


		for (int n=0;n<N;n++)
		{
			row[n]=0;
					
		}
		for(int m=0;m<M;m++)
		{
			col[m]=0;
		}
		for (int n=0;n<N;n++)
		{
			for(int m=0;m<M;m++)
			{
				if(lawn[n][m]>=row[n])
				{
					row[n]=lawn[n][m];
				}
				if(lawn[n][m]>=col[m])
				{
					col[m]=lawn[n][m];
				}
			
			}
		
		}
		flag=true;
		for (int n=0;n<N;n++)
		{
			if(flag==false)
			{
				break;
			}
			for(int m=0;m<M;m++)
			{
				if(lawn[n][m]<row[n]&&lawn[n][m]<col[m])
				{
					flag=false;
					break;
				}

			
			}
		
		}
		if(flag==true)
		{
			fprintf(fout,"Case #%d: YES\n",t);
		}
		else
		{
			fprintf(fout,"Case #%d: NO\n",t);
		}




	
	
	}



	return 0;
}

