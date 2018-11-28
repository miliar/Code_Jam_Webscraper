#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,smax,ct,ct1;
	cin>>t;
	char arr[1002];
	for(int j=1;j<=t;j++)
	{
		ct=0;
		ct1=0;
		cin>>smax;
		cin>>arr;
		for(int i=0;i<=smax;i++)
		{
				if(ct<i)
				{
					ct1+=i-ct;
					ct+=i-ct;
				}
				ct+=arr[i]-48;
		}
		cout<<"Case #"<<j<<": "<<ct1<<"\n";
	}
	return 0;
}