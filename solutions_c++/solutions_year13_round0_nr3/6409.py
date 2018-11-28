#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;
long long a,b,t,count,root;
int num[100];
bool isP(long long x)
{
	long long m=1,d=0;
	while(x/m != 0) {m*=10;d++;}
	for(long long i=(d-1);i>=0;i--)
	{
		num[i]=x%10;
		x=x/10;
	}
	for(int i=0;i<(d - 1 - i);i++)
	{
		if(num[i]!=num[d-1-i]) return false;
	}
	return true;
}
int main()
{
	ifstream in;
	ofstream out;
	in.open("in.txt");
	out.open("out.txt");
	in>>t;
	for(int k=1;k<=t;k++)
	{
		in>>a>>b;
		count=0;
		root= (long long)sqrt(a);
		if(root*root != a)
		{
			a=root;
			a++;
		}
		else
		{
			a=root;
		}
		b=(long long)sqrt(b);
		for(int i=a;i<=b;i++)
		{
			if(isP(i) && isP(i*i))
			{
				count++;
			}
		}
		out<<"Case #"<<k<<": "<<count<<endl;
	}
	return 0;
}