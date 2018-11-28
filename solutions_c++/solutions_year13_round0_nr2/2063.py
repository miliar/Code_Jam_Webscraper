#include<stdio.h>

int pattern_match(int ptrn[101][101],int init[101][101],int row[101],int col[101],int r,int c);

int main()
{
	int t,n,m,i,j,k,ptrn[101][101],init[101][101];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		int row[101]={0},col[101]={0};
		scanf("%d%d",&n,&m);		
		for(j=0;j<n;j++)
			for(k=0;k<m;k++)
			{
				scanf("%d",&ptrn[j][k]);
				init[j][k]=100;
				if(row[j]<ptrn[j][k])
					row[j] = ptrn[j][k]; 
				if(col[k]<ptrn[j][k])
					col[k] = ptrn[j][k];
			}
		if(pattern_match(ptrn,init,row,col,n,m))
			printf("Case #%d: YES\n",i);
		else
			printf("Case #%d: NO\n",i);
	}
	return 0;
}

int pattern_match(int ptrn[101][101],int init[101][101],int row[101],int col[101],int r,int c)
{
	int i,j,x,col1[101]={0},mc[101]={1000};
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
			init[i][j] = row[i]; 			
	}	
	for(i=0;i<c;i++)	
		for(j=0;j<r;j++)			
			if(init[j][i] > col[i])
				init[j][i] = col[i]; 			
	
	for(i=0;i<r;i++)
		for(j=0;j<c;j++)			
			if(init[i][j]!=ptrn[i][j])
				return 0;			
	return 1;
}
