#include <stdio.h>
#include <string.h>
#define nMax 8

char m[nMax][nMax];
int flagX=0,flagO=0;//flag X,O,inital lose;
void printm()
{
	printf("print input:\n");
	for(int i=0; i<=3; i++)
	{
		for(int j=0; j<=3; j++)
		{
			printf("%c",m[i][j]);
		}	
		printf("\n");
	}
}

void judge()//O win return 0,X win return 1,Draw return 2,not completed reutn 3;
{
	int i,j;
	//成段扫描4+4+2可能；
	for(i=0; i<4; i++) //横的四种可能 
	{
		for(j=0; j<4; j++)
		{
			if(m[i][j]=='X'||m[i][j]=='T')
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
	//竖的四种可能 
	
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
			if(m[j][i]=='O'||m[j][i]=='T')
			{
				continue;
			}
			else
			{
				break;
			}
		}
		if(j==4) {flagO=1;}
	}
	//两条对角线
	for(i=0;i<4; i++)
	{
		if(m[i][i]=='X'||m[i][i]=='T')
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
		
	/**0000**/
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
	//printf("\nflagO:%d,flagX:%d,cntP:%d\n",flagO,flagX,cntP);
	if(flagO==1&&flagX==0)
		printf("O won\n");
	if(flagO==0&&flagX==1)
		printf("X won\n");
	if((flagO==1&&flagX==1&&cntP==0)||(flagO==0&&flagX==0&&cntP==0))
		printf("Draw\n");
	if(flagO==0&&flagX==0&&cntP==1)
		printf("Game has not completed\n");
}
int main(int argc, char *argv[])
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		memset(m,0,sizeof(m));//formate map m;
		flagX=0,flagO=0;//flag X,O,inital lose;
		for(int j=0;j<=3;j++)
		{
			for(int k=0; k<=3; k++)
			{
				scanf(" %c",&m[j][k]);
			}
		}
		//printm();
		printf("Case #%d: ",i);
		judge();
	}
	return 0;
}
