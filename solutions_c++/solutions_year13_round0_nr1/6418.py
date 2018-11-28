#include<stdio.h>
#include<memory.h>
#include<string.h>
int n;
char board[1001][5][5];
int ans;

int positioncomputespecific(int a,char c)
{
int i,j,k;

for(i=0;i<=3;i++)
	{
		for(j=0;j<=3;j++)
		{
		if(board[a][i][j]!=c&&board[a][i][j]!='T')
		break;
		}
	if(j==4)
	return(1);
	}


for(i=0;i<=3;i++)
	{
		for(j=0;j<=3;j++)
		{
		if(board[a][j][i]!=c&&board[a][j][i]!='T')
		break;
		}
	if(j==4)
	return(1);
	}

for(i=0;i<=3;i++)
	{
	if(board[a][i][i]!=c&&board[a][i][i]!='T')
	break;
	}
if(i==4) return(1);

for(i=0;i<=3;i++)
	{
	if(board[a][i][3-i]!=c&&board[a][i][3-i]!='T')
	break;
	}
if(i==4) return(1);

return(0);
}

int checkdot(int a)
{
int i,j,k;
for(i=0;i<=3;i++)
	{
		for(j=0;j<=3;j++)
		{
		if(board[a][i][j]=='.')
		return(1);
		}
	}
return(0);
}


int positioncompute(int a)
{
if(positioncomputespecific(a,'X')) return (1);
if(positioncomputespecific(a,'O')) return (2);
if(checkdot(a)) return(4);
return(3);
}

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, tc;
	int cnt;
	fscanf(fp, "%d", &n);
	for(i=0;i<n;i++) 
		{
		for(j=0;j<=3;j++)
		fscanf(fp, "%s", &board[i][j][0]);
		}
	
	for(i=0;i<n;i++) 
		{

		ans=positioncompute(i);
		if(ans==1)	
		fprintf(ofp, "Case #%d: X won\n",i+1);		
		if(ans==2)	
		fprintf(ofp, "Case #%d: O won\n",i+1);		
		if(ans==3)	
		fprintf(ofp, "Case #%d: Draw\n",i+1);		
		if(ans==4)	
		fprintf(ofp, "Case #%d: Game has not completed\n",i+1);		
		}

	return 0;
}
