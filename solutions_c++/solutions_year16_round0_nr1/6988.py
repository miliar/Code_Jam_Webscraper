#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int check(int m, int array[])
{
	int a;
	while(m>0)
	{
		a = m%10;
		m/=10;
		array[a] = 1;
		//cout<<a<<" "<<m;
	}
	
	int flag = 1;
	for(int i =0; i<10;i++)
	{
		if(array[i]!=1)
			flag = 0;
	}
	return flag;
}
int main()
{
	int t,n;
	cin>>t;
	for(int i =1;i<=t;i++)
	{
		cin>>n;
		if(n ==0) 
		{cout<<"Case #"<<i<<": INSOMNIA"<<endl;continue;}
		int m = n;
		int array[10] = {0};
		while(check(m,array) == 0)
		{
			m+=n;
		}
		cout<<"Case #"<<i<<": "<<m<<endl;
	}
	return 0;
}		
		
