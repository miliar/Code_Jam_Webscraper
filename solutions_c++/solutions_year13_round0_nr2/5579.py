#include<stdio.h>

#include<math.h>
#include<climits>
#include <iomanip> //forsetw()
using namespace std;

#define gi(x) scanf("%d",&x)


int b[100][100];
int p[100][100];
int m,n;
char *ans[2]={"YES","NO"};
void print(int a[100][100])
{
	for(int x=0;x<n;x++)
	{
		printf("\n");
		for(int y=0;y<m;y++)
			printf("%d ",a[x][y]);
	}
	printf("\n\n");
}
char *solve_small()
{
	int x,y;
	for(x=0;x<n;x++)
		for(y=0;y<m;y++)
			p[x][y]=2;
	
	//first row.. col down
	for(x=0;x<m;x++)
	{
		int e=b[0][x];
		bool flag=true;
		for(y=0;y<n;y++)
			if(b[y][x]>e || p[y][x]<e)
			{
				flag=false;
				break;
			}
		if(flag)
			for(y=0;y<n;y++)
				p[y][x]=e;
			
	}	
	//print(p);
	//last row,col up
	for(x=0;x<m;x++)
	{
		int e=b[n-1][x];
		bool flag=true;
		for(y=n-1;y>=0;y--)
			if(b[y][x]>e || p[y][x]<e)
			{
				flag=false;
				break;
			}
		if(flag)
			for(y=n-1;y>=0;y--)
				p[y][x]=e;
			
	}
	//print(p);
	//first col, row to right
	for(x=0;x<n;x++)
	{
		int e=b[x][0];
		bool flag=true;
		for(y=0;y<m;y++)
			if((b[x][y]>e ) || (p[x][y]<e))
			{
				flag=false;
				break;
			}
		if(flag)
			for(y=0;y<m;y++)
				p[x][y]=e;
			
	}
	//print(p);
	//last col, row to left
	for(x=0;x<n;x++)
	{
		int e=b[x][m-1];
		bool flag=true;
		for(y=0;y<m;y++)
			if(b[x][y]>e || p[x][y]<e)
			{
				flag=false;
				break;
			}
		if(flag)
			for(y=0;y<m;y++)
				p[x][y]=e;
			
	}
	//print(p);
	
	//check if p and b are same
	for(x=0;x<n;x++)
		for(y=0;y<m;y++)
			if(b[x][y]!=p[x][y])
				return ans[1];
	return ans[0];					
		
}
int main(int argc,char **argv)
{
	int t,i,x,y;
	//freopen("input.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	gi(t);
	while(getchar()!='\n');
	for(i=0;i<t;i++)
	{
		scanf("%d%d",&n,&m);
		for(x=0;x<n;x++)
		{
			while(getchar()!='\n');
			for(y=0;y<m;y++)
				scanf("%d",&b[x][y]);
		}
		printf("Case #%d: %s\n",i+1,solve_small());	
		
	}
	
	return 0;
}

