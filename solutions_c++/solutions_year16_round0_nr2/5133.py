#include <iostream>
#include<string.h>
#include<new>
#include <cstdio>

using namespace std;

int flag =0,count = 0;

int find_minus_from_last(string in)
{
	int len,i;
	len = in.size();
	for(i=len-1;i>=0;)
	{
		if (in[i]=='+')
			i--;
		else
			return i;
	}
	return -1;
}
void swap (string *in, int pos)
{
	for(int i=0;i<=pos;i++)
	{
		if(in->at(i)=='-')
			in->at(i)= '+';
		else
			in->at(i)= '-';
	}
	flag=1;
}
void func(int s, string in)
{
	int val;
	val = find_minus_from_last(in);
	if(val==-1)
	{
		if(flag==0)
			cout<<"Case #"<<s+1<<": 0"<<endl;
		else
			cout<<"Case #"<<s+1<<": "<<count<<endl;
	}
	else
	{
		swap(&in,val);
		count++;
		func(s,in);
	}
}


int main() {
	freopen("a.in","rt",stdin);
	freopen("ab.out","wt",stdout);
	int n;
	string in;
	char *ptr;
	cin>>n;
	for(int s=0;s<n;s++)
	{
		string in;
		int val;
		cin>>in;
		func(s,in);
		flag = 0;
		count=0;
	}
	return 0;
}
