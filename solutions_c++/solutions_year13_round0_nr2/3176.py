#include<iostream>
#include<cstdio>

using namespace std;
int board[101][101];
int check();
int T,N,M;
void main()
{
	freopen("B-large.in","r",stdin);
	freopen("b_large.out","w",stdout);
	cin>>T;
	for(int i=0;i!=T;++i)
	{
		cin>>N>>M;
		for(int j=0;j!=N;++j)
		{
			for(int k=0;k!=M;++k)
			{
				cin>>board[j][k];
			}
		}
		if(check())
			cout<<"Case #"<<i+1<<": YES"<<endl;
		else
			cout<<"Case #"<<i+1<<": NO"<<endl;
	}
}
int check()
{
	int i,j,k;
	int tag;
	for(i=0;i!=N;++i)
	{
		for(j=0;j!=M;++j)
		{
			tag=0;
			for(k=0;k!=M;++k)
			{
				if(board[i][j] < board[i][k])
				{
					tag++;
					break;
				}
			}
			for(k=0;k!=N;++k)
			{
				if(board[i][j] < board[k][j])
				{
					tag++;
					break;
				}
			}
			if(tag==2)
				return 0;
		}
	}
	return 1;
}