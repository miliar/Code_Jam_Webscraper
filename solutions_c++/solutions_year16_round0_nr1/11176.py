#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<memory.h>
using namespace std;
//Brute Force
bool a[10];
void pArr()
{
	for(int i=0;i<10;i++)
	{
		cout<<a[i]<<"  ";
	}
}
void checkDigits(unsigned long long int n)
{
	while(n!=0)
	{
		a[n%10]=true;
		n/=10;
	}
}
bool cAN()
{
	for(int i=0;i<10;i++)
	{
		if(a[i]==false)
		return false;
	}
	return true;
}
unsigned long long int calculateLastNum(unsigned long long int n)
{
	if(n==0)
	return 0;
	int i=0;
	while(++i)
	{
		if(!cAN())
		{
			checkDigits(n*i);
		}
		else
			return n*(i-1);	
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		for(int i=0;i<10;i++){
			a[i]=false;
		}
		unsigned long long int n;
		scanf("%llu",&n);
		unsigned long long int p=0;	
		if((p=calculateLastNum(n))==0)
		printf("Case #%d: INSOMNIA\n",j);
		else
		printf("Case #%d: %llu\n",j, p);
	}
	return 0;
}
