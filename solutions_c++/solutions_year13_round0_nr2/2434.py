#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<set>

int pos(int p[100][100],int l[100][100],int n,int m,int num,int *i,int *j)
{
	for(int k=0;k<n;k++)
	{
		for(int q=0;q<m;q++)
		{
			if(p[k][q]==num)
			{
				if(p[k][q]!=l[k][q])
				{
					*i=k;
					*j=q;
					return 1;
				}
			}
		}
	}
	return 0;
}
int possible(int p[100][100],int l[100][100],int n,int m,int i,int j,int num,int row)
{	
	if(row)
	{
		for(int x=0;x<m;x++)
		{
			if(num < p[i][x])
			{
				return 0;
			}
		}
	}
	else
	{
		for(int x=0;x<n;x++)
		{
			if(num < p[x][j])
				return 0;
		}
	}
	return 1;
}
int main()
{
	int t,n,m;
	freopen("bin.txt","r",stdin);
	freopen("bout.txt","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int p[100][100],l[100][100]={0},max=0;
		std::set<int, std::greater<int>> nums;
		std::set<int, std::greater<int>>::iterator it;
		scanf("%d %d",&n,&m);
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<m;k++)
			{
				scanf("%d",&p[j][k]);
				if(max<p[j][k])
					max=p[j][k];
				nums.insert(p[j][k]);
			}
		}
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<m;k++)
			{
				l[j][k]=max;
			}
		}
		it=nums.begin();
		it++;
		while(it!=nums.end())
		{
			int num=*it;
			int r,c;
			if(pos(p,l,n,m,num,&r,&c))
			{	
				if(possible(p,l,n,m,r,c,num,1))
				{
					for(int x=0;x<m;x++)
					{
						l[r][x]=num;
					}
				}
				else if(possible(p,l,n,m,r,c,num,0))
				{
					for(int x=0;x<n;x++)
					{
						l[x][c]=num;
					}
				}
				else
					break;
			}
			else
			{
				it++;
			}
		}
		printf("Case #%d: ",i);
		if(it==nums.end())
			printf("YES");
		else
			printf("NO");
		printf("\n");
	}
	return 0;
}