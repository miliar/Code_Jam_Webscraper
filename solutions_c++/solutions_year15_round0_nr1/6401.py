#include<iostream>
#include<vector>
#include<stdio.h>
#include<string.h>
using namespace std;
int a[2000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,Smx;
	string str;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>Smx;
		cin>>str;
	
		for(int i=0;i<str.length();i++)
			a[i]=str[i]-'0';
			
		int count=0;
		int numOfFriend=0;
		
		for(int i=0;i<str.length();i++)
		{
			int temp=0;
			
			if(i>count)
			{
				temp=i-count;
				numOfFriend+=temp;
			}
			count=count+temp+a[i];
			
		}
		cout<<"Case #"<<k<<": "<<numOfFriend<<endl;
	}
		
    
}
