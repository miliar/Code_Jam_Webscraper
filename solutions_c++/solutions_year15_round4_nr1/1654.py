#include<cstdio>
using namespace std;
char ar[103][103];
int R,C;
int code(int i,int j)
{
	if(ar[i][j]=='>') return 1;
	if(ar[i][j]=='v') return 2;
	if(ar[i][j]=='<') return 3;
	if(ar[i][j]=='^') return 4;
}

int in_r_c(int x,int y)
{
	int cc=0;
	for(int i=0;i<R;i++)
		   if(ar[i][y]!='.') cc++;
		   
		   if(cc>1) return 1;
		   cc=0;
	for(int i=0;i<C;i++)
		   if(ar[x][i]!='.') cc++;
		   
		   if(cc>1) return 1;
		   
		   return 0;
}
int check(int x,int y)
{
	int s=code(x,y);
	if(s==1)
	{
		for(int i=y+1;i<C;i++)
	{
		if(ar[x][i]!='.') return 1;
	}
	return 0;
	}
	
	if(s==2)
	{
		for(int i=x+1;i<R;i++)
	{
		if(ar[i][y]!='.') return 1;
	}
	return 0;
	}
	
	if(s==3)
	{
		for(int i=y-1;i>=0;i--)
	{
		if(ar[x][i]!='.') return 1;
	}
	return 0;
	}
	if(s==4)
	{
			for(int i=x-1;i>=0;i--)
	{
		if(ar[i][y]!='.') return 1;
	}
	return 0;
		
	}
	
}
int main()
{
	int ntc; scanf("%d",&ntc);
	for(int tc=1;tc<=ntc;tc++)
	{
	printf("Case #%d: ",tc);
	scanf("%d %d",&R,&C);
	for(int i=0;i<R;i++)
	for(int j=0;j<C;j++)
	{
		scanf(" %c ",&ar[i][j]);
	}
	int ans=0;
	int f=1;
	for(int i=0;i<R;i++)
	for(int j=0;j<C;j++)
	{
		if(ar[i][j]=='.') continue;
		int t= check(i,j);
		
		if(t==1) continue;
		
	
		if(in_r_c(i,j)) ans++; 
		else
		{
			f=0; break;
		}
	}
	if(f==0) printf("IMPOSSIBLE\n");
	else printf("%d\n",ans);
	
	
	}
}
