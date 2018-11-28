#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

bool f(bool judge[10])
{
	for(int i=0;i<10;i++)
	{
		if(judge[i]==false)
			return false;
	}
	return true;

}



void f1(long int x,bool judge[10])
{
	while(x>0)
	{
		long int temp=x % 10;
		judge[temp]=1;
		x=x/10;
	}
}

int f2(long int x,bool judge[10])
{
	long int temp=x;
	for(int i=0;i<300;i++)
	{
		f1(temp,judge);
		if(f(judge)==true)
			return temp;
		temp=temp+x;
	}
	return -1;
}



int main()
{
	ifstream q("A-large.in");
	ofstream o("output.txt");

	long int T=0;
	long int N=0;
	q>>T;
	for(long int i=1;i<=T;i++)
	{
		bool judge[10];
		for(int j=0;j<10;j++)
			judge[j]=0;
		q>>N;
		long int temp=f2(N,judge);
		if(temp==-1)
			o<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
			o<<"Case #"<<i<<": "<<temp<<endl;
	}

}