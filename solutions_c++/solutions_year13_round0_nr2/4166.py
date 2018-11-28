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
	for(int f=1;f<=T;++f)
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
			int bi=a[i][0];
			for(int j=1;j<M;j++)
			{
				if(bi<a[i][j])
					bi=a[i][j];
			}
			for(int j=0;j<M;j++)
			{
				if(bi<b[i][j])
					b[i][j]=bi;
			}
		}
		for(int j=0;j<M;j++)
		{
			int bi=a[0][j];
			for(int i=1;i<N;i++)
			{
				if(bi<a[i][j])
					bi=a[i][j];
			}
			for(int i=0;i<N;i++)
			{
				if(bi<b[i][j])
					b[i][j]=bi;
			}
		}
		int check=0;
		for(int i=0;i<N && !check;i++)
		{
			for(int j=0;j<M && !check;j++)
			{
				if(a[i][j]!=b[i][j])
					check=1;
			}
		}
		if(check)
			cout<<"Case #"<<f<<": NO\n";
		else
			cout<<"Case #"<<f<<": YES\n";
	}
	getch();
}