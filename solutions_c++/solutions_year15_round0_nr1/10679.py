#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("in1.in","r",stdin);
	freopen("out1.txt","w",stdout);
	int t;
	cin>>t;
	int f=t;
	while(t--)
	{
		int x;
		cin>>x;
		char c;
		int count=0,total=0;
		for(int i=0;i<x+1;i++)
		{
			cin>>c;
			if(c!=48 && i-total>0){
			count+=(i-total);total+=count;}
			total+=(c-48);
		}
		cout<<"Case #"<<f-t<<": "<<count<<endl;
	}
	return 0;
}

