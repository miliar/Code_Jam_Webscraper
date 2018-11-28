#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

long long int a[1006][1008],flg,n,m,c;
char s[1006][1008];

void rec(long long int x,long long int y)
{
	long long int i,j,k;
	if(a[x][y]==0 && flg==1)
	{
		//printf("%lld %lld %lld\n",i,j,k);
		if(s[x][y]=='^')
		{
			i=x;j=y;k=0;
			while(1)
			{
				i--;
				if(i==-1)
				break;
				if(s[i][j]!='.')
				{
					k=1;
					a[x][y]=1;
					rec(i,j);
					break;
				}
			}
		}
		
		if(s[x][y]=='v')
		{
			i=x;j=y;k=0;
			while(1)
			{
				i++;
				if(i==n)
				break;
				if(s[i][j]!='.')
				{
					k=1;
					a[x][y]=1;
					rec(i,j);
					break;
				}
			}
		}
		
		if(s[x][y]=='<')
		{
			i=x;j=y;k=0;
			while(1)
			{
				j--;
				if(j==-1)
				break;
				if(s[i][j]!='.')
				{
					k=1;
					a[x][y]=1;
					rec(i,j);
					break;
				}
			}
		}
		
		if(s[x][y]=='>')
		{
			i=x;j=y;k=0;
			while(1)
			{
				j++;
				if(j==m)
				break;
				if(s[i][j]!='.')
				{
					k=1;
					a[x][y]=1;
					rec(i,j);
					break;
				}
			}
		}
		//printf("%lld %lld %lld %lld\n",i,j,k,c);
		if(k==0)
		{
			c++;
			
			i=x-1;
			j=y;
			while(1)
			{
				if(i==-1)
				break;
				if(s[i][j]!='.')
				{
					a[x][y]=1;
					k=1;
					rec(i,j);
					break;
				}
				i--;
			}
		}
		
		if(k==0)
		{
			
			i=x+1;
			j=y;
			while(1)
			{
				if(i==n)
				break;
				if(s[i][j]!='.')
				{
					a[x][y]=1;
					k=1;
					rec(i,j);
					break;
				}
				i++;
			}
		}
		
		if(k==0)
		{
			
			i=x;
			j=y-1;
			while(1)
			{
				if(j==-1)
				break;
				if(s[i][j]!='.')
				{
					a[x][y]=1;
					k=1;
					rec(i,j);
					break;
				}
				j--;
			}
		}
		
		if(k==0)
		{
			
			i=x;
			j=y+1;
			while(1)
			{
				if(j==m)
				break;
				if(s[i][j]!='.')
				{
					a[x][y]=1;
					k=1;
					rec(i,j);
					break;
				}
				j++;
			}
		}
		
		if(k==0)
		flg=0;
	}
}

int main()
{
	freopen("abc.txt","r",stdin);
	freopen("test.txt","w",stdout);
	long long int f,f1,i,j;
	scanf("%lld",&f);
	for(f1=1;f1<=f;f1++)
	{
		scanf("%lld %lld",&n,&m);
		for(i=0;i<n;i++)
		scanf("%s",s[i]);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				a[i][j]=0;
			}
		}
		//printf("a");
		flg=1;c=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(s[i][j]!='.' && a[i][j]==0)
				{
				//	printf("a");
					rec(i,j);
				}
			}
		}
		printf("Case #%lld: ",f1);
		if(flg==0)
		printf("IMPOSSIBLE\n");
		else
		printf("%lld\n",c);
	}
	return 0;
}
