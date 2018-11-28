#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define nMax 8

char m[nMax][nMax];
int flagX=0,flagO=0;
FILE *fp,*fp1;


void run()
{
	int i,j;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
		{
			if(m[i][j]=='X'||m[i][j]=='T') continue;
			else break;
		}
		if(j==4)
		{
			flagX=1;
			continue;
		}
		
		for(j=0; j<4; j++)
		{
			if(m[i][j]=='O'||m[i][j]=='T')
			{
				continue;
			}
			else
			{
				break;
			}
		}
		if(j==4)
		{
			flagO=1;
		}				
	}

	for(i=0; i<4;i++)
	{
		for(j=0; j<4; j++)
		{
			if(m[j][i]=='X'||m[j][i]=='T')
			{
				continue;
			}
			else
			{
				break;
			}
		}
		if(j==4)
		{
			flagX=1;
			continue;
		}
	    for(j=0; j<4; j++)
		{
			if(m[j][i]=='O'||m[j][i]=='T') continue;
			else break;
		}
		if(j==4) {flagO=1;}
	}
	for(i=0;i<4; i++)
	{
		if(m[i][i]=='X'||m[i][i]=='T')	continue;
		else break;
	}
	if(i==4)
	{
		flagX=1;
	}

	for(i=0;i<4; i++)
	{
		if(m[i][i]=='O'||m[i][i]=='T')
		{
			continue;
		}
		else
		{
			break;
		}
	}
	if(i==4)
	{
		flagO=1;
	}

	for(i=0; i<4; i++)
	{
		if(m[i][3-i]=='O'||m[i][3-i]=='T')
		{
			continue;
		}
		else
		{
			break;
		}
	}
	if(i==4)
	{
		flagO=1;
	}
	for(i=0; i<4; i++)
	{
		if(m[i][3-i]=='X'||m[i][3-i]=='T')
		{
			continue;
		}
		else
		{
			break;
		}
	}
	if(i==4)
	{
		flagX=1;
	}	
	int cntP=0;
	for(i=0;i<4;i++)
	{
		for(j=0; j<4; j++)
		{
			if(m[i][j]=='.')
			{
				cntP=1;
				break;
			}
		}
		if(cntP==1) break;
	}
	if(flagO==1&&flagX==0)
		fprintf(fp1,"O won\n");
	if(flagO==0&&flagX==1)
		fprintf(fp1,"X won\n");
	if((flagO==1&&flagX==1&&cntP==0)||(flagO==0&&flagX==0&&cntP==0))
		fprintf(fp1,"Draw\n");
	if(flagO==0&&flagX==0&&cntP==1)
		fprintf(fp1,"Game has not completed\n");
}
int main()
{
	int t;
	fp=fopen("A-large (1).in","r");
	fp1=fopen("A.out","w");
	fscanf(fp,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		memset(m,0,sizeof(m));
		flagX=0,flagO=0;
		for(int j=0;j<=3;j++)
		{
			for(int k=0; k<=3; k++)
			{
				fscanf(fp," %c",&m[j][k]);
			}
		}
		fprintf(fp1,"Case #%d: ",i);
		run();
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}
