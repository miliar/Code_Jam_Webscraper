#include<stdio.h>

int m,n;
void row_max(int lawn[][101],int pattern[][101],int row)
{
int max=0,j;	
	for(j=0;j<m;j++)
	{
		if(pattern[row][j]>max)
			max=pattern[row][j];
	}
	for(j=0;j<m;j++)
			lawn[row][j] = max;
	
}

void col_max(int lawn[][101],int pattern[][101],int col)
{
int max=0,j;	
	for(j=0;j<n;j++)
	{
		if(pattern[j][col]>max)
			max=pattern[j][col];
	}
	for(j=0;j<n;j++)
	{
		if(lawn[j][col] > max)
			lawn[j][col] = max;	
	}
}

int check(int lawn[][101],int pattern[][101])
{
int j,k;
 	for(j=0;j<n;j++)
		for(k=0;k<m;k++)
			if(lawn[j][k]!= pattern[j][k])	
					return 0;
	return 1;
}
int main()
{
	int t,lawn[101][101],pattern[101][101],i,j,k;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		for(j=0;j<n;j++)
			for(k=0;k<m;k++)
				lawn[j][k]=100;
				
		scanf("%d%d",&n,&m);
		for(j=0;j<n;j++)
			for(k=0;k<m;k++)
				scanf("%d",&pattern[j][k]);
		for(j=0;j<n;j++)
			row_max(lawn,pattern,j);
		for(j=0;j<m;j++)
			col_max(lawn,pattern,j);
	
		if(check(lawn,pattern))
			printf("Case #%d: YES\n",i);
		else
			printf("Case #%d: NO\n",i);
	}
return 0;
}

