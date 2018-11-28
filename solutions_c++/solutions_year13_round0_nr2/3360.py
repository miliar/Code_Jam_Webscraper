#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int checkv(int grnd[][100], int i, int j, int m)
{
	int x;
	for(x=0;x<m;x++)
	{
		if(grnd[i][j]<grnd[i][x])
			return 1;
	}
	return 0;
}

int checkh(int grnd[][100], int i, int j, int n)
{
	int x;
	for(x=0;x<n;x++)
	{
		if(grnd[i][j]<grnd[x][j])
			return 1;
	}
	return 0;
}

string check(int grnd[][100], int n, int m)
{
	int i,j;
	int s=0;
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		{
			s=s+(checkv(grnd,i,j,m)*checkh(grnd,i,j,n));
		}
	if(s>0)
		return ": NO\n";
	else return ": YES\n";
}



int main()
{
	int i,j,k,n;
	int N=0,M=0;
	int grnd[100][100];
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("outout.in");
	in >> n;
	string line;
	getline(in, line);
	for(k=0;k<n;k++)
	{
		in >> N;
		in >> M;
		getline(in, line);
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				in >> grnd[i][j];
			}
			getline(in, line);
		}
		out << "Case #" << k+1 << check(grnd,N,M);
	}
	in.close();
	out.close();
	return 0;
}