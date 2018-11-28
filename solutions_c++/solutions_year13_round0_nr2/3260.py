#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int func();
int findres(int rowno,int colno);

int N,M;
int A[100][100];
int main()
{
	int res;
	int T;
	fin>>T;
	int i=0;
	int x,y;
	while(i<T)
	{
		fin>>N;
		fin>>M;
		for(x=0;x<N;x++)
		{
			for(y=0;y<M;y++)
			{
				fin>>A[x][y];
			}
		}
		res=func();
		i++;
		fout<<"Case #";
		fout<<i;
		fout<<": ";
		if(res==0){fout<<"NO";}
		else{fout<<"YES";}

		if(i<T){fout<<"\n";}
	}
	return(0);
}

int func()
{
	int i,j;
	int res;
	for(i=0;i<N;i++)
	{
		for(j=0;j<M;j++)
		{
			res=findres(i,j);
			if(res==0){return(0);}
		}
	}
	return(1);
}

int findres(int rowno,int colno)
{
	int maxlen=A[rowno][colno];
	int i,j;

	
	//Rowwise chk
	int chk1=0;
	i=rowno;
	for(j=0;j<M;j++)
	{
		if(A[i][j]>maxlen){chk1++;}
	}
	if(chk1==0){return(1);}

	//Col chk
	chk1=0;
	j=colno;
	for(i=0;i<N;i++)
	{
		if(A[i][j]>maxlen){chk1++;}
	}
	if(chk1==0){return(1);}
	return(0);
}