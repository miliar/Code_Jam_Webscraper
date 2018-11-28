#include<fstream>
#include<vector>
#include<string>
#include<iostream>
using namespace std;

string z_ans(int N,int M,int (*a)[100])
{
	int n1=N-1,m1=M-1;
	int maxN[100],maxM[100];
	for(int i=0;i<N;i++)maxN[i]=0;
	for(int i=0;i<M;i++)maxM[i]=0;
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
		{
			if(maxN[i]>a[i][j]&&maxM[j]>a[i][j])return "NO";
			if(maxN[i]<a[i][j])maxN[i]=a[i][j];
			if(maxM[j]<a[i][j])maxM[j]=a[i][j];
		}
	}
	//for(int i=0;i<N;i++)cout<<maxN[i];
	//cout<<endl;
	//for(int i=0;i<M;i++)cout<<maxM[i];
	//cout<<endl;
	return "YES";
}
int main()
{
	ifstream ifile("input.txt");
	ofstream ofile("output.txt");
	int T,N,M;
	int a[100][100];
	ifile>>T;
	for(int i=1;i<=T;i++)
	{
		ifile>>N>>M;
		
		for(int j=0;j<N;j++)
		{
			for(int k=0;k<M;k++)
			{
				ifile>>a[j][k];
			}
		}
		ofile<<"Case #"<<i<<": "<<z_ans(N,M,a)<<endl;
	}
}