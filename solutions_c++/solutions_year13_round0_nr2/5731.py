#include<iostream>
#include<fstream>
using namespace std;
char* lawn[20];
int N,M;
bool allOnes(int p,int q)
{
	bool ret1=true;
	bool ret2=true;
	for(int i=0;i<2*M-1;i=i+2)
		{
			if(lawn[p][i]!='1')
				ret1=false;
		}
	for(int i=0;i<N;i++)
		{
			if(lawn[i][q]!='1')
				ret2=false;
		}
	return (ret1||ret2);
}
bool isPossible()
{
for(int i=0;i<N;i++)
	for(int j=0;j<2*M-1;j=j+2)
	{
	if(lawn[i][j]=='1')
	{
		if(!allOnes(i,j))
			return false;
	}
	}
	return true;
}
int main()
{
	for(int j=0;j<20;j++)
	{lawn[j]=new char[40];
	}
char Tstring[10];
int T;
char sizestring[10];
ifstream iff;
ofstream off;
iff.open("C:\\Users\\him\\Desktop\\GOOGLE\\B-small-attempt1.in");
off.open("C:\\Users\\him\\Desktop\\GOOGLE\\output.txt");
iff.getline(Tstring,9);
T=atoi(Tstring);
for(int i=0;i<T;i++)
{
iff.getline(sizestring,9,' ');
N=atoi(sizestring);
iff.getline(sizestring,9);
M=atoi(sizestring);
for(int j=0;j<N;j++)
	{
	iff.getline(lawn[j],39);
	}
cout<<"N= "<<N<<" M= "<<M<<"\n";
for(int j=0;j<N;j++)
	cout<<lawn[j]<<"\n";
off<<"Case #"<<i+1<<": "<<(isPossible()?"YES":"NO")<<"\n";

}
iff.close();
off.close();
system("pause");
}