#include<bits/stdc++.h>
using namespace std;
int a[20];
int r,c,n;

int mat[17][17];
int ans;

void eval(int k)
{
	int co=0;
	for(int i=0; i<k; i++)
	{
		if(a[i]==1)
		co++;
	}
	
	if(co!=n)
	return ;
	
	for(int i=0; i<=r; i++)
	{
		for(int j=0; j<=c; j++)
		mat[i][j]=0;
	}
	
	for(int i=0; i<k; i++)
	{
		if(a[i]==1)
		{
			int x,y;
			y=(i%c);
			if(y==0)
			y=c;
			x=(i/c);
			mat[x+1][y]=1;
		}
	}
	
	int cc=0;
	for(int i=1; i<=c; i++)
	{
		for(int j=1; j<r; j++)
		{
			if(mat[j][i]==1 && mat[j+1][i]==1)
			cc++;
		}
	}
	
	for(int i=1; i<=r; i++)
	{
		for(int j=1; j<c; j++)
		{
			if(mat[i][j]==1 && mat[i][j+1]==1)
			cc++;
		}
	}
	
	if(cc<ans)
	ans=cc;
}
void subsets(int j, int k)
{
	if(j==k)
	eval(k);
	else
	{
		a[j]=1;
		subsets(j+1, k);
		a[j]=0;
		subsets(j+1, k);
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d %d %d", &r, &c, &n);
		int k=r*c;
		
		for(int i=0; i<=18; i++)
		a[i]=0;
		
		ans=10000000;
		
		subsets(0, k);
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
