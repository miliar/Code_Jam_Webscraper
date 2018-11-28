#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

ofstream o("output.txt");


bool isprime(long long int a)
{
	long long int temp=0;
	if(a % 2==0)
		return false;
	for(long long int i=3;i<=sqrt(a);i=i+2)
	{
		if(a % i==0)
			return false;
	}
	return true;
}

long long int first(long long int a)
{
	long long int temp=0;
	for(long long int i=2;i<a;i++)
	{
		if(a % i==0)
			return i;
	}
	return -1;
}

long long int value(int *a,int N,int sel)
{
	long long int value=0;
	long long int temp=1;
	for(int i=N-1;i>=0;i--)
	{
		value=value+a[i]*temp;
		temp=temp*sel;
	}
	return value;
}


bool fun(int *a,int N)
{
	long long int cache[9];
	for(int i=0;i<9;i++)
		cache[i]=0;
	for(int i=2;i<=10;i++)
	{
		long long int v=value(a,N,i);
		if(isprime(v)==true)
		{
			return false;
		}
		else
		{
			cache[i-2]=first(v);
		}
	}
	for(int i=0;i<N;i++)
		o<<a[i];
	for(int i=0;i<9;i++)
		o<<' '<<cache[i];
	o<<endl;
	return true;
}

bool every1(int *a,int N)
{
	for(int i=0;i<N;i++)
	{
		if(a[i]==0)
			return false;
	}
	return true;
}

void next(int *a,int N)
{
	if(every1(a,N)==true)
		return;
	for(int i=N-2;i>0;i--)
	{
		if(a[i]==0)
		{
			a[i]=1;
			return;
		}
		if(a[i]==1)
		{
			a[i]=0;
			continue;
		}
	}
}


int main()
{
	ifstream f("C-small-attempt2.in");
	int T=0;
	int N=0;
	int J=0;
	f>>T;
	f>>N;
	f>>J;

	int *a;
	a=new int[N];
	
	a[0]=1;
	a[N-1]=1;
	for(int i=1;i<N-1;i++)
		a[i]=0;
	o<<"Case #1:"<<endl;
	int count=0;
	while(1)
	{
		if(fun(a,N)==true)
		{
			count++;
			next(a,N);
		}
		else
		{
			next(a,N);
		}
		if(count==J)
			break;

	}
	
}