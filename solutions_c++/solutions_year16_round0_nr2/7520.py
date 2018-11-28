#include<iostream>
#include<string.h>
using namespace std;
char a[1000];
int check(int n)
{
	for(int i=0;i<n;i++)
	{
		if(a[i]=='-')
		return 0;
	}
	return 1;
}
void calculate(int n)
{
	for(int i=0;i<n;i++)
	{
		if(a[i]=='-')
		a[i]='+';
		else
		a[i]='-';	
	}

		
}
void operate(int n)
{
	int i=0;
	if(a[i]=='-')
	{
	
	while(a[i]=='-'&&i<n)
	{
	i++;}
	calculate(i);
}
else if(a[i]=='+')
{
	while(a[i]=='+'&&i<n)
	{
	i++;}
	calculate(i);
}
	
}
int main()
{
	int t,i,n,j,m;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>a;
		int k=0,c=0;
		n=strlen(a);
		k=check(n);
		while(k!=1)
		{
			c++;
			operate(n);
			k=check(n);
		}
		
		cout<<"Case #"<<i<<": "<<c<<endl;
		
	}
}