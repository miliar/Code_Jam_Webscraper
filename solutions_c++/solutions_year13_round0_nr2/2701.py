#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;
	scanf("%d", &t);
	for( int p=0; p<t; p++)
	{
		bool row[101],col[101];
		bool flag4=false;
		int A[101][101];
		int N,M,a=0,mini=100;
		scanf("%d", &N);
		scanf("%d", &M);
		for( int i=0; i<100; i++)
		{
			row[i]=false;
			col[i]=false;
		}
		for( int i=0; i<N; i++)
		{
			for( int j=0; j<M; j++)
			{
				int temp;
				scanf("%d", &temp);
				A[i][j]=temp;
			}
		}
		bool flag=true;
		bool flag1=true;
		while(flag)
		{
			mini=100;
			for( int i=0; i<N; i++)
			{
				if(row[i]==false)
				{
					for( int j=0; j<M; j++)
					{
						if(col[j]==false)
							mini=min(A[i][j],mini);
					}
				}
			}
			flag=false;
			for( int i=0; i<N; i++)
			{
				if(row[i]==false)
				{
					for( int j=0; j<M; j++)
					{
						if(col[j]==false)
						{
							if(A[i][j]!=mini)
								break;
						}
						if(j==M-1)
						{
							row[i]=true;
							flag=true;
						}
					}
				}
			}
			if(flag==true ||flag1==true)
			{
				mini=100;
				for( int i=0; i<N; i++)
				{
					if(row[i]==false)
					{
						for( int j=0; j<M; j++)
						{
							if(col[j]==false)
								mini=min(A[i][j],mini);
						}
					}
				}
				flag1=false;
				flag=false;
				for( int j=0; j<M; j++)
				{
					if(col[j]==false)
					{
						for( int i=0; i<N; i++)
						{
							if(row[i]==false)
							{
								if(A[i][j]!=mini)
									break;
							}
							if(i==N-1)
							{
								col[j]=true;
								flag=true;
							}
						}
					}
				}
			}
			bool flag3=false;
			for( int i=0; i<N; i++)
			{
				if(row[i]==false)
				{
					break;
				}
				if(i==N-1)
					flag3=true;
			}
			for( int i=0; i<M; i++)
			{
				if(col[i]==false)
					break;
				if(i==M-1)
					flag4=true;
			}
			if(flag4==true)
				break;
		}
		if(flag4)
		printf("Case #%d: YES\n", p+1);
		else
		printf("Case #%d: NO\n", p+1);
	}
}
