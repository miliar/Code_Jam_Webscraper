//By Sainath
#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
int main()
{
	FILE *in=fopen("text.in","r");
	FILE *out=fopen("text.out","w");
	int t;
	fscanf(in,"%d",&t);
	for(int cc=1;cc<=t;cc++)
	{
		int first;
		int second;
		int fmatrix[4][4];
		int smatrix[4][4];
		fscanf(in,"%d",&first);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fscanf(in,"%d",&fmatrix[i][j]);
			}
		}
		fscanf(in,"%d",&second);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fscanf(in,"%d",&smatrix[i][j]);
			}
		}
		vector<int> common;
		for(int i=0;i<4;i++)
		{
			int present=fmatrix[first-1][i];
			for(int j=0;j<4;j++)
			{
				if(smatrix[second-1][j]==present)
					common.push_back(present);
			}
		}
		if(common.size()==0)
		{
			fprintf(out,"Case #%d: Volunteer cheated!\n",cc );
		}
		else if(common.size()>1)
		{
			fprintf(out,"Case #%d: Bad magician!\n",cc );
		}
		else
		{
			fprintf(out,"Case #%d: %d\n",cc,common[0] );
		}
	}

}
