#include <iostream>
#include <cstdio>
using namespace std;
int checkrow(int **,int,int);
int checkcol(int **,int,int);
bool check(int **,int **,int ,int);
int main()
{
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
	int T;
	cin>>T;
	int M,N;
	for(int caseno=1;caseno<=T;++caseno)
	{
		cin>>N>>M;
		int **pdest = new int*[N];
		int **pinit = new int*[N];
		for(int i=0;i<N;++i)
		{
			pdest[i] = new int[M];
			pinit[i] = new int[M];
		} 
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<M;++j)
			{
				cin>>pdest[i][j];
				pinit[i][j]=100;
			}
		}
		cout<<"Case #"<<caseno<<": ";
		for(int i=0;i<N;++i)
		{
			int desth = checkrow(pdest,i,M);
			for(int j=0;j<M;++j)
			{
				pinit[i][j] = desth;
			}
		}
		for(int i=0;i<M;++i)
		{
			if(checkcol(pdest,i,N)==2)
				continue;
			for(int j=0;j<N;++j)
			{
				pinit[j][i]=1;
			}
		}
		if(check(pdest,pinit,N,M)==true)
		{
			cout<<"YES"<<endl;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}
	return 0;
}

int checkrow(int **p,int row,int flag)
{
	//max = 0;
	for(int i=0;i<flag;++i)
	{
		if(p[row][i]==2)
		{
			return 2;	
		}
	}
	return 1;
}
int checkcol(int **p,int col,int flag)
{
	//max = 0;
	for(int i=0;i<flag;++i)
	{
		if(p[i][col]==2)
		{
			return 2;	
		}
	}
	return 1;
}
bool check(int **pdest,int **pinit,int N,int M)
{
	for(int i=0;i<N;++i)
	{
		for(int j=0;j<M;++j)
		{
			if(pdest[i][j]!=pinit[i][j])
				return false;
		}
	}
	return true;
}
