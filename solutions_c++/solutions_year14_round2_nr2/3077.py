#include<iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int x=0;x<T;x++)
	{
		int a,b,k,ct=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
					ct++;
			}
		}
		cout<<"Case #"<<x+1<<": "<<ct<<endl;
	}
	return 0;
}
