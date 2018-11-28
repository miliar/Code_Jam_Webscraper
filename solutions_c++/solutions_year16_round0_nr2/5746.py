#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void reverse(bool s[101], int n)
{
	bool temp[101];
	for(int i=1;i<=n;i++)
	{
		temp[i]=!s[i];
	}
	for(int i=1;i<=n;i++)
	{
		s[i]=temp[n-i+1];
	}
}

bool judge(bool s[101],int len)
{
	for(int i=1;i<=len;i++)
	{
		if(s[i]==0)
			return false;
	}
	return true;
}

int fun(bool s[101],int len)
{
	int count=1;
	int sum=0;
	if(judge(s,len)==true)
		return sum;
	for(int i=1;i<=len;i++)
	{
		if(s[i]==s[i+1])
		{
			count++;
			continue;
		}
		else
		{
			reverse(s,count);
			count++;
			sum++;
			if(judge(s,len)==true)
				return sum;
		}
	}

	if(s[1]==0)
	{
		reverse(s,len);
		sum++;
	}

	return sum;
}

int main()
{
	ifstream f("B-large.in");
	ofstream o("pancakeout.txt");
	int T=0;
	f>>T;
	for(int j=1;j<=T;j++)
	{
		bool s[101];
		string x;
		f>>x;
		int len=x.length();
		for(int i=1;i<=len;i++)
		{
			if(x[i-1]=='+')
				s[i]=1;
			if(x[i-1]=='-')
				s[i]=0;
		}
		int temp=fun(s,len);
		o<<"Case #"<<j<<": "<<temp<<endl;

	}

}