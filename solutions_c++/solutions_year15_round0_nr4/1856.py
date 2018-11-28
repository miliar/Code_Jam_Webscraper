#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int A[5][5][5];
	int count=0;
	freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			A[1][i][j]=2;
			count++;
		}
	}
	
	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			A[2][i][j]=2;
			count++;
		}
	}
	A[2][1][1]=A[2][3][1]=A[2][1][3]=A[2][3][3]=1;

	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			A[3][i][j]=1;
			count++;
		}
	}
	for(int i=2;i<=4;i++)
	{
		A[3][i][3]=2;
		A[3][3][i]=2;
	}

	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			A[4][i][j]=1;
			count++;
		}
	}
	A[4][3][4]=A[4][4][3]=A[4][4][4]=2;
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int x,y,z;
		cin>>x>>y>>z;
		if(A[x][y][z]==1)
		{
			cout<<"Case #"<<i+1<<": RICHARD";
		}
		if(A[x][y][z]==2)
		{
			cout<<"Case #"<<i+1<<": GABRIEL";
		}
		cout<<endl;
	}
}