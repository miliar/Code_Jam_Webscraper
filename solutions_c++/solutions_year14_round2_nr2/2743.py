#include <iostream>

using namespace std;

int main()
{
int T;
cin>>T;
	for (int ct=0;ct<T;ct++)
	{
	int a,b,k;
	cin>>a>>b>>k;
	int count=0;
		for (int i=a-1;i>=0;i--)
		{
			for (int j=b-1;j>=0;j--)
			{
				if ((i&j)<k) count++;
			}
		}
	cout<<"Case #"<<ct+1<<": "<<count<<endl;
	}
}
