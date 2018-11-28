
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <fstream>
using namespace std;

int SqrtNum(int x)
{
	int q;
	q=sqrt(x);
	if(q*q==x)
		return q;
	else
		return -1;
}

int Huiwen(long n)
{
	if(n==-1)
		return 0;
	else
	{
	long t1=0,t2=n;
	while(n>0)
	{t1=t1*10+n%10;
		 n=n/10; 
	 }
	if(t1==t2) return 1;
		else return 0;
	}
}
 
int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("out.txt");
	int N;
	fin>>N;
	for(int j=1;j<=N;j++)
	{
		int count=0;
		int a,b;
		fin>>a;
		fin>>b;
		for(int num=a;num<=b;num++)
		{
		if(Huiwen(num)==1 && Huiwen(SqrtNum(num))==1)
			count++;
		}

		fout<<"Case #"<<j<<":"<<" "<<count<<endl;

	}

}
