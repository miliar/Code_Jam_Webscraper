#include<iostream>
#include<conio.h>
using namespace std;
void main()
{
	int T;
	cin>>T;
	int M,N;
	int a[100][100];
	int b[100][100];
	for(int x=1;x<=T;++x)
	{
		cin>>N>>M;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				cin>>a[i][j];
				b[i][j]=100;
			}
		}
		for(int i=0;i<N;i++)
		{
			int big=a[i][0];
			for(int j=1;j<M;j++)
			{
				if(big<a[i][j])
					big=a[i][j];
			}
			for(int j=0;j<M;j++)
			{
				if(big<b[i][j])
					b[i][j]=big;
			}
		}
		for(int j=0;j<M;j++)
		{
			int big=a[0][j];
			for(int i=1;i<N;i++)
			{
				if(big<a[i][j])
					big=a[i][j];
			}
			for(int i=0;i<N;i++)
			{
				if(big<b[i][j])
					b[i][j]=big;
			}
		}
		int flag=0;
		for(int i=0;i<N && !flag;i++)
		{
			for(int j=0;j<M && !flag;j++)
			{
				if(a[i][j]!=b[i][j])
					flag=1;
			}
		}
		if(flag)
			cout<<"Case #"<<x<<": NO\n";
		else
			cout<<"Case #"<<x<<": YES\n";
	}
}