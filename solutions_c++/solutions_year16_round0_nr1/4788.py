#include<fstream>
#include<iostream>
using namespace std;
int arr[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
void assig(long N)
{
		int t;
	while(N!=0)
	{
		t=N%10;
		arr[t]=t;
		N=N/10;
	}	
}
int check(long N)
{
	assig(N);
	for(int i=0;i<10;i++)
	{
			if(arr[i]!=i)
					return 1;			
	}
		return 0;
}
int main()
{
	int T;long N;int j=0;int m;
	ifstream fin("A-large.in",ios::in);
	ofstream fout("Output.txt",ios::app);
	if(!fin)
	{
			cout<<"ERROR!";
	}
	fin>>T;
	for(int i=0;i<T;i++)
	{
		j=0;
		fin>>N;
		long M=N;
		while(j!=1)
		{
			if(N==0)
			{
				fout<<"Case #"<<i+1<<": "<<"INSOMNIA\n";
				j=1;
			}
			m=check(M);
			if(m==0)
			{
				fout<<"Case #"<<i+1<<": "<<M<<"\n";
				for(int i=0;i<10;i++)
						arr[i]=-1;
				j=1;				
			}
			else
			{
				M=M+N;
			}		
		}
	}	
	fin.close();
	fout.close();
	return 0;
}
