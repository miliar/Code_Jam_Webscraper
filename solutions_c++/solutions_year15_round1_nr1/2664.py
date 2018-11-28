#include<iostream>
#include<conio.h>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<iomanip>
#include<cstdlib>
#include<cmath>
#define uli unsigned long long
#define sz (int)1e7+1
using namespace std;
int arr[100000];
void doit()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	int a=0;
	for(int i=0;i<n-1;i++)
	{
		if((arr[i]-arr[i+1])>0)
		{
			a=a+(arr[i]-arr[i+1]);
		}
	}
	cout<<a<<" ";
	int final=0;
	int min=0;
	for(int i=0;i<n-1;i++)
	{
		if(min<(arr[i]-arr[i+1]))
		min=arr[i]-arr[i+1];
	}
	for(int i=0;i<n-1;i++)
	{
	//	arr[i]+=rem;
//		cout<<"final"<<final<<endl;
		if((min-arr[i])>=0)
		{
			final=final+arr[i];
		}
		else
		{
			final=final+min;
	//		rem=arr[i]-min;
		}
	}
	cout<<final;
}
int main()
{
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cout<<"case #"<<i<<": ";
		doit();
		cout<<endl;
	}
	return 0;
}
