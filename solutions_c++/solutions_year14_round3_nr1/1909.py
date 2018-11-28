#include<iostream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<cmath>
using namespace std;
int po2(int a,int &count)
{
	while(a%2==0)
	{
		a=a/2;
		count++;
	}
	return a;
}
int pl(int a)
{
	int c=0;
	while(pow(2,c+1)<=a) c++;
	return c;
}

int main()
{
	int t;cin>>t;
	
	for(int i=0;i<t;i++)
	{
	int x=0,count=0;
	string s,s1;
	cin>>s;
	while(s[x+1]!='/') x++;
	
	s1=s.substr(0,x+1);
	int a=atoi(s1.c_str());
	
	s1=s.substr(x+2);
	int b=atoi(s1.c_str());
	int p=po2(b,count);
	//cout<<a<<p<<count<<endl;
	if(p==1){
		if(a>1) cout<<"Case #"<<i+1<<": "<<count-pl(a)<<endl;
		else cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	
	else{
		if(a%p==0){
			if(a/p==1) cout<<"Case #"<<i+1<<": "<<count<<endl;
			else cout<<"Case #"<<i+1<<": "<<count-1<<endl;
		}
		else cout<<"Case #"<<i+1<<": "<<"impossible"<<endl;
}}
	
}

		
