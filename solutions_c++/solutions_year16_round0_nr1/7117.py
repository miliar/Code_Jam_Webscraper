#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main(){
	
	int t;
	ifstream pe("A-large.in");
	ofstream out("outu.out");
	pe>>t;
	for(int q=0;q<t;q++)
	{
		int ar[10]={0};
		int n,a,b,c,count=0,i=1;
		pe>>n;
		if(n==0)
		{
			out<<"Case #"<<q+1<<": "<<"INSOMNIA"<<"\n";continue;
		}
		for( i=1;;i++)
		{
			count=0;
			a=n*i;
			while(a>0)
			{
				++ar[a%10];
				a/=10;
			}
			
			for(int j=0;j<10;j++)
			{
				if(ar[j]!=0)
				++count;
			}
			if(count==10)
			break;
			
		}
		out<<"Case #"<<q+1<<": "<<n*i<<"\n";
		
		
	}
	
	return 0;
}
