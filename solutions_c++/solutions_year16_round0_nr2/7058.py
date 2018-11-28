#include <iostream>
#include <conio.h>
#include <string>
#include <string.h>
using namespace std;
int f()
{
	string a;
	cin>>a;
	char symbol=a[0], find;
	int counter=0;
	int len;
	len=a.length();
	for(int i=1;i<len;i++)
	{
		if(symbol=='+')
			find='-';
		else
		find='+';
		if(a[i]==find)
		{
			counter++;
			symbol=find;
		}			
	}
		if(a[len-1]=='+')
			return counter;
		else
			return ++counter;
}
int main()
{
	int a;
	cin>>a;
	int out[a];
	for(int j=0;j<a;j++)
	{
		out[j]=f();
	}
	for (int i=0;i<a;i++)
	{
		cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	}
	return 0;
}
