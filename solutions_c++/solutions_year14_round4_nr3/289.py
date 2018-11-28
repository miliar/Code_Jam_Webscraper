#include <stdio.h>

int a[110][510];
int w ,h ,ww ,hh;
int dfs(int x ,int y ,int p)
{
	a[x][y]=1;
	if (y==h)
	{
		return 1;	
	}
	else
	{
		if (p==1)
		{
			if (a[x-1][y]==0)
			{
				if (dfs(x-1,y,3))
				{
					return 1;	
				}
			}
			if (a[x][y+1]==0)
			{
				if (dfs(x,y+1,1))
				{
					return 1;	
				}
			}
			if (a[x+1][y]==0)
			{
				if (dfs(x+1,y,4))
				{
					return 1;	
				}
			}					
		}
		else if (p==2)
		{
			if (a[x+1][y]==0)
			{
				if (dfs(x+1,y,4))
				{
					return 1;	
				}
			}
			if (a[x][y-1]==0)
			{
				if (dfs(x,y-1,2))
				{
					return 1;	
				}
			}			
			if (a[x-1][y]==0)
			{
				if (dfs(x-1,y,3))
				{
					return 1;	
				}
			}						
		}
		else if (p==3)
		{
			if (a[x][y-1]==0)
			{
				if (dfs(x,y-1,2))
				{
					return 1;	
				}
			}
			if (a[x-1][y]==0)
			{
				if (dfs(x-1,y,3))
				{
					return 1;	
				}
			}			
			if (a[x][y+1]==0)
			{
				if (dfs(x,y+1,1))
				{
					return 1;	
				}
			}							
		}
		else
		{
			if (a[x][y+1]==0)
			{
				if (dfs(x,y+1,1))
				{
					return 1;	
				}
			}			
			if (a[x+1][y]==0)
			{
				if (dfs(x+1,y,4))
				{
					return 1;	
				}
			}			
			if (a[x][y-1]==0)
			{
				if (dfs(x,y-1,2))
				{
					return 1;	
				}
			}			
		}
		return 0;
	}
}
int main(void)
{
	int t ,i;
	int b;
	int x1 ,y1 ,x2 ,y2;
	int j ,j1 ,j2;
	int ans;
	
	FILE *outfile=fopen("out1.txt","w");
	scanf("%d" ,&t);
	for (i=1 ; i<=t ; i++)
	{
		scanf("%d %d %d" ,&w ,&h ,&b);
		ww=w+1;
		hh=h+1;
		for (j1=1 ; j1<=w ; j1++)
		{
			for (j2=1 ; j2<=h ; j2++)	
			{
				a[j1][j2]=0;	
			}
		}
		for (j1=0 ; j1<=ww ; j1++)
		{
			a[j1][0]=-1;
			a[j1][hh]=-1;	
		}
		for (j2=0 ; j2<=hh ; j2++)
		{
			a[0][j2]=-1;
			a[ww][j2]=-1;	
		}		
		for (j=1 ; j<=b ; j++)
		{
			scanf("%d %d %d %d" ,&x1 ,&y1 ,&x2 ,&y2);
			x1++;
			y1++;
			x2++;
			y2++;
			for (j1=x1 ; j1<=x2 ; j1++)
			{
				for (j2=y1 ; j2<=y2 ; j2++)
				{
					a[j1][j2]=-1;	
				}
			}
		}
		ans=0;
		for (j=1 ; j<=w ; j++)
		{
			if (a[j][1]==0)
			{
				if (dfs(j,1,1))
				{
					ans++;
				}
			}
		}
		printf("%d\n" ,i);
		fprintf(outfile ,"Case #%d: %d\n" ,i ,ans);
	}
	fclose(outfile);

	return 0;
}
